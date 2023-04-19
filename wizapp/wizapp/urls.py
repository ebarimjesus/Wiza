from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.http import HttpResponse

from django.urls import path
from django.views.generic.base import RedirectView
from talkgpt.views import talkgpt, send_message, stream_response

urlpatterns += [
    path("talkgpt/", talkgpt, name="talkgpt"),
    path("send_message/", send_message, name="send_message"),
    path("stream_response/", stream_response, name="stream_response"),
    path('send_message', RedirectView.as_view(url='/send_message/', permanent=True)),
]


