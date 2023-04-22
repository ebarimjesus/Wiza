from django.urls import include, path
from django.views.generic import RedirectView
from django.views import View
from . import views

from .views import (
    send_message, 
    stream_response,
    LandingPageView, 
    ExamplesPageView, 
    talkgpt, editor, 
    image_generator, 
    dalle, 
    TranscriberView, 
    CoderView, 
    generate_code,  
    process_input,
    get_audio,
    play_audio,
    recognize_speech_from_mic,
    get_voice_options, 
    set_voice_option
)

app_name = 'talkgpt'

urlpatterns = [
    path('send_message/', send_message, name='send_message'),
    path('stream_response/', stream_response, name='stream_response'),
    path('send_message', RedirectView.as_view(url='/send_message/', permanent=True)),
    path('', LandingPageView.as_view(), name='landing'),
    path('talkgpt/', talkgpt, name='talkgpt'),
    path('examples/', ExamplesPageView.as_view(), name='examples'),
    path('editor/', views.editor, name='editor'),
    path('image_generator/', views.image_generator, name='image_generator'),
    path('dalle/', views.dalle, name='dalle'),
    path('transcriber/', TranscriberView.as_view(), name='transcriber'),
    path('coder/', CoderView.as_view(), name='coder'),
    path('generate_code/', generate_code, name='generate_code'),
    path('process_input/', process_input, name='process_input'),
    path('get-audio/', get_audio, name='get_audio'),
    path('play-audio/', play_audio, name='play_audio'),
    path('recognize_speech_from_mic/', recognize_speech_from_mic, name='recognize_speech_from_mic'),
    path('get_voice_options/', get_voice_options, name='get_voice_options'),
    path('set_voice_option/<str:option_id>/', set_voice_option, name='set_voice_option'),
]    




