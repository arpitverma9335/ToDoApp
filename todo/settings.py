import os
import django_heroku
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'staticfiles/js', 'serviceworker.js')

SECRET_KEY = os.environ['secret_key_todo']

DEBUG = False

ALLOWED_HOSTS = ['regularly.herokuapp.com']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['user_email']
EMAIL_HOST_PASSWORD = os.environ['user_pass']

INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'django.contrib.sites',
      'Auth',
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'allauth.socialaccount.providers.google',
      'compressor',
      'pwa',
      ]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

PWA_APP_NAME = 'Regularly'
PWA_APP_DESCRIPTION = "Simple To-Do Web Application" 
PWA_APP_THEME_COLOR = '#0A0302' 
PWA_APP_BACKGROUND_COLOR = '#000' 
PWA_APP_DISPLAY = 'standalone' 
PWA_APP_ID = '/' 
PWA_APP_ORIENTATION = 'portrait' 
PWA_APP_START_URL = '/' 
PWA_APP_STATUS_BAR_COLOR = 'default' 
PWA_APP_ICONS = [ { 'src': '/static/img/icon_512x512.png', 'sizes': '512x512', "purpose": "any"},
                   { 'src': '/static/img/icon_512x512.png', 'sizes': '512x512', "purpose": "maskable"},
                   { 'src': '/static/img/icon_192x192.png', 'sizes': '192x192', "purpose": "any"},
                   { 'src': '/static/img/icon_192x192.png', 'sizes': '192x192', "purpose": "maskable"},
                   { 'src': '/static/img/icon_160x160.png', 'sizes': '160x160', "purpose": "any"},
                   { 'src': '/static/img/icon_160x160.png', 'sizes': '160x160', "purpose": "maskable"},
                   { 'src': '/static/img/icon_148x148.png', 'sizes': '148x148', "purpose": "any"},
                   { 'src': '/static/img/icon_148x148.png', 'sizes': '148x148', "purpose": "maskable"},
                   { 'src': '/static/img/icon_96x96.png', 'sizes': '96x96', "purpose": "any"} ,
                   { 'src': '/static/img/icon_96x96.png', 'sizes': '96x96', "purpose": "maskable"} ,
                   { 'src': '/static/img/icon_48x48.png', 'sizes': '48x48', "purpose": "any"} ,
                   { 'src': '/static/img/icon_48x48.png', 'sizes': '48x48', "purpose": "maskable"} ,
                   { 'src': '/static/img/icon_32x32.png', 'sizes': '32x32', "purpose": "any"} ,
                   { 'src': '/static/img/icon_32x32.png', 'sizes': '32x32', "purpose": "maskable"} ,
                ] 
PWA_APP_ICONS_APPLE = [ { 'src': '/static/img/icon_192x192.png', 'sizes': '192x192'},
                        { 'src': '/static/img/icon_160x160.png', 'sizes': '160x160'},
                        { 'src': '/static/img/icon_148x148.png', 'sizes': '148x148'},
                        { 'src': '/static/img/icon_96x96.png', 'sizes': '96x96'} ,
                        { 'src': '/static/img/icon_48x48.png', 'sizes': '48x48'} ,
                        { 'src': '/static/img/icon_32x32.png', 'sizes': '32x32'} ] 

PWA_APP_SPLASH_SCREEN = [ { 'src': '/static/img/icon_512x512.png', 'sizes': '512x512'} ] 
PWA_APP_DIR = 'ltr' 
PWA_APP_LANG = 'en-US'

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSP_DEFAULT_SRC = ["'self'", '*']
CSP_SCRIPT_SRC = [
    "'self' https: 'unsafe-inline'",
    'https://cdnjs.cloudflare.com',
]
CSP_STYLE_SRC = [
    "'self' https: 'unsafe-inline'",
]

SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000

if DEBUG is False:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True


ROOT_URLCONF = 'todo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'csp.context_processors.nonce',
            ],
        },
    },
]

WSGI_APPLICATION = 'todo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'auth',
        'USER': 'postgres' ,
        'PASSWORD': os.environ['db_pass'],
        'HOST': 'localhost',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'static_content')
      ]
STATIC_ROOT = os.path.join(BASE_DIR , 'assets')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_FILTERS = {
    'css':[
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter',
    ],
    'js':[
        'compressor.filters.jsmin.JSMinFilter',
    ]
}
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False

django_heroku.settings(locals())