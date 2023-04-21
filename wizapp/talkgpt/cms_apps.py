from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from talkgpt.cms_appconfig import TalkGptConfig
from django.urls import re_path, include
from .views import LandingPageView, ExamplesPageView, talkgpt


@apphook_pool.register  # register the application

class TalkGptApphook(CMSApp):
    app_name = "talkgpt"
    name = "TalkGpt Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            re_path(r'^$', LandingPageView.as_view(), name='landing'),
            re_path(r'examples/$', ExamplesPageView.as_view(), name='examples'),
            re_path(r'^talkgpt/$', talkgpt, name='talkgpt')
        ]



