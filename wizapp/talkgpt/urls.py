from django.urls import path
from . import views
from .views import LandingPageView

app_name = 'talkgpt'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('talkgpt/', views.talkgpt, name='talkgpt'),
    # other URL patterns specific to the talkgpt app
]


