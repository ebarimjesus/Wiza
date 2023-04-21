from django.urls import path
from . import views
from .views import LandingPageView
from .views import ExamplesPageView



app_name = 'talkgpt'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('talkgpt/', views.talkgpt, name='talkgpt'),
    path('examples/', ExamplesPageView.as_view(), name='examples'),
]


