from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from django.urls import path, include
from talkgpt.views import LandingPageView, ExamplesPageView, talkgpt


class TalkGptConfig(CMSApp):
    app_name = 'talkgpt'
    name = _('TalkGpt')

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path('', LandingPageView.as_view(), name='landing'),
            path('examples/', ExamplesPageView.as_view(), name='examples'),
            path('talkgpt/', talkgpt, name='talkgpt'),
        ]
    

apphook_pool.register(TalkGptConfig)  # register the application





