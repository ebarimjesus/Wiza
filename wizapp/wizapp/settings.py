from django.utils.translation import gettext_lazy as _


from django.utils.translation import gettext_noop
import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for wizapp project.

Generated by 'django-admin startproject' using Django 3.1.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'tuys+s5dky+x5d(@b0y4+rh!f8gio#6-$d(e!3u)^&o=!-*_ej'
SECRET_KEY_FALLBACKS = []
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'wizapp.urls'
WSGI_APPLICATION = 'wizapp.wsgi.application'
AUTH_PASSWORD_VALIDATORS = [{'NAME':
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    }, {'NAME':
    'django.contrib.auth.password_validation.MinimumLengthValidator'}, {
    'NAME':
    'django.contrib.auth.password_validation.CommonPasswordValidator'}, {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
    ]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Etc/UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
STATICFILES_DIRS = os.path.join(BASE_DIR, 'wizapp', 'static'),
SITE_ID = 1
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'wizapp', 'templates')], 'OPTIONS': {
    'context_processors': ['django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.i18n',
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.template.context_processors.media',
    'django.template.context_processors.csrf',
    'django.template.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.template.context_processors.static',
    'cms.context_processors.cms_settings'], 'loaders': [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader']}}]
MIDDLEWARE = ['cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware']
INSTALLED_APPS = ['djangocms_admin_style', 'django.contrib.auth',
    'django.contrib.contenttypes', 'django.contrib.sessions',
    'django.contrib.admin', 'django.contrib.sites',
    'django.contrib.sitemaps', 'django.contrib.staticfiles',
    'django.contrib.messages', 'corsheaders', 'cms', 'menus', 'sekizai',
    'treebeard', 'djangocms_text_ckeditor', 'filer', 'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities', 'djangocms_file',
    'djangocms_icon', 'djangocms_link', 'djangocms_picture',
    'djangocms_style', 'djangocms_googlemap', 'djangocms_video',
    'email_validator', 'wizapp', 'talkgpt', 'aldryn_apphooks_config',
    'parler', 'taggit', 'taggit_autosuggest', 'meta', 'djangocms_blog',
    'sortedm2m', 'aldryn_search', 'faq', 'profiles' ]

LANGUAGES = [('af', gettext_noop('Afrikaans')), ('ar', gettext_noop(
    'Arabic')), ('ar-dz', gettext_noop('Algerian Arabic')), ('ast',
    gettext_noop('Asturian')), ('az', gettext_noop('Azerbaijani')), ('bg',
    gettext_noop('Bulgarian')), ('be', gettext_noop('Belarusian')), ('bn',
    gettext_noop('Bengali')), ('br', gettext_noop('Breton')), ('bs',
    gettext_noop('Bosnian')), ('ca', gettext_noop('Catalan')), ('ckb',
    gettext_noop('Central Kurdish (Sorani)')), ('cs', gettext_noop('Czech')
    ), ('cy', gettext_noop('Welsh')), ('da', gettext_noop('Danish')), ('de',
    gettext_noop('German')), ('dsb', gettext_noop('Lower Sorbian')), ('el',
    gettext_noop('Greek')), ('en', gettext_noop('English')), ('en-au',
    gettext_noop('Australian English')), ('en-gb', gettext_noop(
    'British English')), ('eo', gettext_noop('Esperanto')), ('es',
    gettext_noop('Spanish')), ('es-ar', gettext_noop('Argentinian Spanish')
    ), ('es-co', gettext_noop('Colombian Spanish')), ('es-mx', gettext_noop
    ('Mexican Spanish')), ('es-ni', gettext_noop('Nicaraguan Spanish')), (
    'es-ve', gettext_noop('Venezuelan Spanish')), ('et', gettext_noop(
    'Estonian')), ('eu', gettext_noop('Basque')), ('fa', gettext_noop(
    'Persian')), ('fi', gettext_noop('Finnish')), ('fr', gettext_noop(
    'French')), ('fy', gettext_noop('Frisian')), ('ga', gettext_noop(
    'Irish')), ('gd', gettext_noop('Scottish Gaelic')), ('gl', gettext_noop
    ('Galician')), ('he', gettext_noop('Hebrew')), ('hi', gettext_noop(
    'Hindi')), ('hr', gettext_noop('Croatian')), ('hsb', gettext_noop(
    'Upper Sorbian')), ('hu', gettext_noop('Hungarian')), ('hy',
    gettext_noop('Armenian')), ('ia', gettext_noop('Interlingua')), ('id',
    gettext_noop('Indonesian')), ('ig', gettext_noop('Igbo')), ('io',
    gettext_noop('Ido')), ('is', gettext_noop('Icelandic')), ('it',
    gettext_noop('Italian')), ('ja', gettext_noop('Japanese')), ('ka',
    gettext_noop('Georgian')), ('kab', gettext_noop('Kabyle')), ('kk',
    gettext_noop('Kazakh')), ('km', gettext_noop('Khmer')), ('kn',
    gettext_noop('Kannada')), ('ko', gettext_noop('Korean')), ('ky',
    gettext_noop('Kyrgyz')), ('lb', gettext_noop('Luxembourgish')), ('lt',
    gettext_noop('Lithuanian')), ('lv', gettext_noop('Latvian')), ('mk',
    gettext_noop('Macedonian')), ('ml', gettext_noop('Malayalam')), ('mn',
    gettext_noop('Mongolian')), ('mr', gettext_noop('Marathi')), ('ms',
    gettext_noop('Malay')), ('my', gettext_noop('Burmese')), ('nb',
    gettext_noop('Norwegian Bokmål')), ('ne', gettext_noop('Nepali')), (
    'nl', gettext_noop('Dutch')), ('nn', gettext_noop('Norwegian Nynorsk')),
    ('os', gettext_noop('Ossetic')), ('pa', gettext_noop('Punjabi')), ('pl',
    gettext_noop('Polish')), ('pt', gettext_noop('Portuguese')), ('pt-br',
    gettext_noop('Brazilian Portuguese')), ('ro', gettext_noop('Romanian')),
    ('ru', gettext_noop('Russian')), ('sk', gettext_noop('Slovak')), ('sl',
    gettext_noop('Slovenian')), ('sq', gettext_noop('Albanian')), ('sr',
    gettext_noop('Serbian')), ('sr-latn', gettext_noop('Serbian Latin')), (
    'sv', gettext_noop('Swedish')), ('sw', gettext_noop('Swahili')), ('ta',
    gettext_noop('Tamil')), ('te', gettext_noop('Telugu')), ('tg',
    gettext_noop('Tajik')), ('th', gettext_noop('Thai')), ('tk',
    gettext_noop('Turkmen')), ('tr', gettext_noop('Turkish')), ('tt',
    gettext_noop('Tatar')), ('udm', gettext_noop('Udmurt')), ('uk',
    gettext_noop('Ukrainian')), ('ur', gettext_noop('Urdu')), ('uz',
    gettext_noop('Uzbek')), ('vi', gettext_noop('Vietnamese')), ('zh-hans',
    gettext_noop('Simplified Chinese')), ('zh-hant', gettext_noop(
    'Traditional Chinese'))]
LANGUAGES_BIDI = ['he', 'ar', 'ar-dz', 'ckb', 'fa', 'ur']
USE_I18N = True
LOCALE_PATHS = []
LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = None
LANGUAGE_COOKIE_DOMAIN = None
LANGUAGE_COOKIE_PATH = '/'
LANGUAGE_COOKIE_SECURE = False
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_SAMESITE = None

CORS_ORIGIN_ALLOW_ALL = True
CMS_TEMPLATES = ('fullwidth.html', 'Fullwidth'), ('sidebar_left.html',
    'Sidebar Left'), ('sidebar_right.html', 'Sidebar Right')
X_FRAME_OPTIONS = 'SAMEORIGIN'
CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}
DATABASES = {'default': {'CONN_HEALTH_CHECKS': 'False', 'CONN_MAX_AGE': 0,
    'ENGINE': 'django.db.backends.sqlite3', 'HOST': 'localhost', 'NAME':
    'project.db', 'PASSWORD': '', 'PORT': '', 'USER': ''}}
THUMBNAIL_PROCESSORS = ('easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters')
META_SITE_PROTOCOL = 'https'
META_USE_SITES = True
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True
META_USE_SCHEMAORG_PROPERTIES = True
AUTH_USER_MODEL = 'auth.User' 


AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'
LOGOUT_REDIRECT_URL = '/'
PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 3
PASSWORD_HASHERS = ['django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher']
AUTH_PASSWORD_VALIDATORS = []
SIGNING_BACKEND = 'django.core.signing.TimestampSigner'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_USE_LOCALTIME = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None
ADMINS = [('Fortune Ebarim', 'ebarim@wiztech.site')]
MANAGERS = ADMINS
FORM_RENDERER = 'django.forms.renderers.DjangoTemplates'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STORAGES = {'default': {'BACKEND':
    'django.core.files.storage.FileSystemStorage'}, 'staticfiles': {
    'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'}}
PASSWORD_HASHERS = ['django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher']

CMS_LANGUAGES = {
    1: [{'code': 'en',
         'fallbacks': ['de', 'fr'],
         'hide_untranslated': False,
         'name': 'English',
         'public': True,
         'redirect_on_fallback': True},
        {'code': 'de',
         'fallbacks': ['en', 'fr'],
         'hide_untranslated': False,
         'name': 'German',
         'public': True,
         'redirect_on_fallback': True},
        {'code': 'fr',
         'fallbacks': ['en', 'de'],
         'hide_untranslated': False,
         'name': 'French',
         'public': True,
         'redirect_on_fallback': True},
        {'code': 'es',
         'fallbacks': ['en', 'de', 'fr'],
         'hide_untranslated': False,
         'name': 'Spanish',
         'public': True,
         'redirect_on_fallback': True},
        {'code': 'pt',
         'fallbacks': ['en', 'de', 'fr'],
         'hide_untranslated': False,
         'name': 'Portuguese',
         'public': True,
         'redirect_on_fallback': True},
        {'code': 'zh-hans',
         'fallbacks': ['en', 'de', 'fr'],
         'hide_untranslated': False,
         'name': 'Simplified Chinese',
         'public': True,
         'redirect_on_fallback': True
        },       
        {'code': 'ar',
         'fallbacks': ['en', 'de', 'fr'],
         'hide_untranslated': False,
         'name': 'Arabic',
         'public': True,
         'redirect_on_fallback': True
        },
        {'code': 'it',
         'fallbacks': ['en', 'de', 'fr'],
         'hide_untranslated': False,
         'name': 'Italian',
         'public': True,
         'redirect_on_fallback': True}],
    'default': {'fallbacks': ['en', 'de', 'fr', 'es', 'pt', 'zh-hans', 'ar', 'it'],
                'hide_untranslated': False,
                'public': True,
                'redirect_on_fallback': True},
}

LANGUAGE_CODE = 'en'
PARLER_DEFAULT_LANGUAGE_CODE = 'en-us'
PARLER_LANGUAGES = {
    None: (
        {'code': 'en',},
        {'code': 'en-us',},
        {'code': 'it',},
        {'code': 'nl',},
    ),
    'default': {
        'fallbacks': ['en'],          # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}

BLOG_AVAILABLE_PERMALINK_STYLES = (
    ('full_date', _('Full date')),
    ('short_date', _('Year /  Month')),
    ('category', _('Category')),
)
BLOG_PERMALINK_URLS = {
    "full_date": "<int:year>/<int:month>/<int:day>/<str:slug>/",
    "short_date": "<int:year>/<int:month>/<str:slug>/",
    "category": "<str:category>/<str:slug>/",
}


BLOG_PLUGIN_TEMPLATE_FOLDERS = (
    ('plugins', _('Default template')),    # reads from templates/djangocms_blog/plugins/
    ('timeline', _('Vertical timeline')),  # reads from templates/djangocms_blog/vertical/
    ('masonry', _('Masonry style')),       # reads from templates/djangocms_blog/masonry/
)



