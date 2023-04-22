
from django.shortcuts import render

from django.http import JsonResponse, FileResponse


import openai
import time
import os
import io
import uuid
import pyttsx3
import ffmpeg
import requests
import speech_recognition as sr

from gtts import gTTS

from django.views.generic import TemplateView
from talkgpt.utils import get_voice_options
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views import View
from django.utils.decorators import method_decorator




openai.api_key = "sk-RDITFbLRYJrcwHFB4A3iuYP6WB1XJ9"



MODEL = "gpt-3.5-turbo-0301"


def get_voice_options(request):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    options = []
    for voice in voices:
        option = {
            'id': voice.id,
            'name': voice.name
        }
        options.append(option)
    return JsonResponse(options, safe=False)


def set_voice_option(request, option_id):
    engine = pyttsx3.init()
    engine.setProperty('voice', option_id)
    return JsonResponse({'success': True})



class LandingPageView(TemplateView):
    template_name = "landing.html"

class ExamplesPageView(TemplateView):
    template_name = "examples.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["voice_options"] = get_voice_options()
        return context

        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voice_options'] = get_voice_options()
        return context



def send_message(request):
    message = request.POST.get('message', '')
    # logic to send the message
    return HttpResponse('Message sent successfully')

 

@csrf_exempt
@require_POST
def talkgpt(request):
    voice_options = get_voice_options(request)
    completion = openai.ChatCompletion.create(
        model=MODEL,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.6,
        messages=[{"role": "user", "content": "Hello!"}]
    )
    response = (completion.choices[0].message)
    return render(request, "talkgpt.html", {"response": response})


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"type": "user", "text": prompt}
        ],
        temperature=0.5,
        max_tokens=3000,
        n=1,
        stop=None,
    )
    return response.choices[0].message.content
    return response


def send_message(request):
    message = request.POST.get("message")
    response = generate_response(message)
    return JsonResponse({"message": response})


def stream_response(prompt):
    prompt = ""  # initialize the prompt variable
    def generate():
        time.sleep(0.5)  # add delay to allow user input to be sent first
        yield "data: {}\n\n".format("Hello! How can I assist you today?")

        while True:
            completions = openai.ChatCompletion.create(
                model=MODEL,
                prompt=prompt,
                max_tokens=3000,
                n=1,
                stop=None,
                temperature=0.5,
            )

            message = completions.choices[0].message
            prompt += message

            yield "data: {}\n\n".format(message)

    return HttpResponse(generate(), content_type="text/event-stream")




def editor(request):
    voice_options = get_voice_options(request)
    return render(request, 'editor.html')

def image_generator(request):
    voice_options = get_voice_options(request)
    return render(request, 'image_generator.html')

@csrf_exempt
def dalle(request):
    # get request data
    data = json.loads(request.body)
    prompt = data.get('prompt')
    image_size = data.get('image_size', 256)
    num_images = data.get('num_images', 4)

    # generate image(s) using DALL-E API
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        n=num_images,
        size=image_size
    )

    # extract image URLs from response
    image_urls = [r.url for r in response.data]

    # edit image(s) using DALL-E API
    edited_images = []
    for url in image_urls:
        edit_response = openai.Image.edit(
            model="image-alpha-001",
            image=url,
            size=image_size,
            operations=["rotate", "resize", "crop", "grayscale"]
        )

        # extract edited image URL from response
        edited_image_url = edit_response.data.url
        edited_images.append(edited_image_url)

    # create HTML with img tags for each edited image
    images_html = ""
    for url in edited_images:
        images_html += f"<img src='{url}' alt='edited image'>"

    # render template with HTML and return as response
    context = {
        'images_html': images_html
    }
    return render(request, 'edited_images.html', context=context)



class TranscriberView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        voice_options = get_voice_options(request)
        return render(request, 'transcribe.html', {'voice_options': voice_options})

class CoderView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        voice_options = get_voice_options(request)
        return render(request, 'coder.html', {'voice_options': voice_options})


@csrf_exempt
def generate_code(request):
    # Get request data
    data = request.POST
    prompt = data.get('prompt')
    language = data.get('language', 'python')
    max_tokens = data.get('max_tokens', 1024)

    # Generate code using OpenAI's Code API
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.2,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Extract code snippet from response
    code_snippet = response.choices[0].text.strip()

    return JsonResponse({'code_snippet': code_snippet})


def generate_audio_file(response_text):
    # Generate a unique filename for the audio file
    filename = str(uuid.uuid4()) + '.wav'
    file_path = os.path.join('audio', filename)

    # Generate the audio file using gTTS
    tts = gTTS(response_text)
    tts.save(file_path)

    # Return the filename so that it can be passed to the play_audio() function
    return filename


def process_input(request):
    user_input = request.json['user_input']
    # Process the user input and generate a response
    response_text = 'Hello, world!'
    filename = generate_audio_file(response_text)
    return JsonResponse({'text': response_text, 'audio_file': filename})


def get_audio(request):
    text = request.json.get('text')
    filename = f'{uuid.uuid4()}.mp3'
    filepath = os.path.join('audio', filename)
    tts = gTTS(text=text)
    tts.save(filepath)
    return JsonResponse({'audio_file_path': f'/static/audio/{filename}'})


def play_audio(request):
    response = request.POST.get('response')
    language = 'en'
    filename = str(uuid.uuid4())
    audio_path = os.path.join('audio', f"{filename}.wav")
    tts = gTTS(text=response, lang=language)
    tts.save(audio_path)
    return FileResponse(open(audio_path, 'rb'))


def recognize_speech_from_mic(request):
    recognizer = sr.Recognizer()

    # get the device index of the default input device
    device_index = None
    for i, name in enumerate(sr.Microphone.list_microphone_names()):
        if 'default' in name:
            device_index = i
            break

    # create a microphone instance using the default input device
    microphone = sr.Microphone(device_index=device_index)

    # adjust the recognizer sensitivity to ambient noise and record audio
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # transcribe the speech
    try:
        transcription = recognizer.recognize_google(audio)
        return JsonResponse({'success': True, 'transcription': transcription})
    except sr.UnknownValueError:
        # speech was unintelligible
        return JsonResponse({'success': False, 'error': 'Unable to recognize speech'})
    except sr.RequestError:
        # API was unreachable or unresponsive
        return JsonResponse({'success': False, 'error': 'API unavailable'})



