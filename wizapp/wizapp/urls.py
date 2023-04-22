from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from talkgpt import views

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from talkgpt.views import (
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

from taggit_autosuggest import urls as taggit_autosuggest_urls

admin.autodiscover()

urlpatterns = [
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    path('admin/', admin.site.urls),
    path('en/talkgpt/', include('talkgpt.urls')),
]

urlpatterns += i18n_patterns(path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
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
    path('taggit_autosuggest/', include(taggit_autosuggest_urls)),
]
