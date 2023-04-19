
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


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

openai.api_key = "


# Create your views here.
MODEL = "gpt-3.5-turbo-0301"


def get_voice_options():
    voices = pyttsx3.init().getProperty('voices')
    voice_options = []
    for voice in voices:
        name = voice.name
        gender = voice.gender
        language = voice.languages[0]
        voice_options.append({'name': name, 'gender': gender, 'language': language})
    return voice_options



def talkgpt(request):
    voice_options = get_voice_options()
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


