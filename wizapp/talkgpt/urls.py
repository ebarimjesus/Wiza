from django.urls import include, path
from .views import LandingPageView, ExamplesPageView, talkgpt

app_name = 'talkgpt'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('talkgpt/', talkgpt, name='talkgpt'),
    path('examples/', ExamplesPageView.as_view(), name='examples'),
]    




