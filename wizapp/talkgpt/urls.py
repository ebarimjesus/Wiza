from django.urls import include, re_path
from . import views
from .views import LandingPageView
from .views import ExamplesPageView
from .views import talkgpt

app_name = 'talkgpt'

urlpatterns = [
    re_path(r'^$', LandingPageView.as_view(), name='landing'),
    re_path(r'^talkgpt/$', talkgpt, name='talkgpt'),
    re_path(r'^examples/$', ExamplesPageView.as_view(), name='examples'),
    re_path(r'^talkgpt/', include('talkgpt.urls', namespace='talkgpt')),
]


