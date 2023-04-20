from django.views.generic.base import RedirectView


from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from talkgpt.views import send_message, stream_response
from talkgpt.views import LandingPageView
from talkgpt.views import ExamplesPageView, talkgpt

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('admin/', admin.site.urls),
    path('en/talkgpt/', include('talkgpt.urls')),
]

urlpatterns += i18n_patterns(path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path("send_message/", send_message, name="send_message"),
    path("stream_response/", stream_response, name="stream_response"),
    path('send_message', RedirectView.as_view(url='/send_message/', permanent=True)),
    path('', LandingPageView.as_view(), name='landing'),
    path('examples/', ExamplesPageView.as_view(), name='examples'),
    path('talkgpt/', talkgpt, name='talkgpt'),
]
