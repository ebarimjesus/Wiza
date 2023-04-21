from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from talkgpt.cms_appconfig import TalkGptConfig


@apphook_pool.register  # register the application
class TalkgptApphook(CMSApp):
    app_name = "talkgpt"
    name = "Talkgpt Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["talkgpt.urls"]

