from pathlib import Path
from dotenv import load_dotenv
import os
from django.utils.translation import gettext_lazy as _


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

# Site Setting
LOGIN_URL  = 'user_auth:login'
LOGIN_REDIRECT_URL  = 'dash:home'
LOGOUT_REDIRECT_URL  = 'user_auth:login'
AUTH_USER_MODEL = "user_auth.User"

ALLOWED_HOSTS = [
    'projectmanager-ylq3.onrender.com',
    '127.0.0.1',
    'manager.m07amed.uk',
]

INSTALLED_APPS = [
    'rosetta',
    'cloudinary',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'django_deep_translator',

    # User Defined apps
    'user_auth',
    'frontend',
    'dashboard',
    
]

ROSETTA_REQUIRES_AUTH = True  # Only allow authenticated users to access Rosetta
ROSETTA_ACCESS_FUNCTION = lambda user: user.is_superuser  # Onl

AUTHENTICATION_BACKENDS = [
    'user_auth.authentication.EmailOrPhoneBackend',  # Custom backend
    'django.contrib.auth.backends.ModelBackend',     # Keep the default one as a fallback
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dashboard.context_processors.user_info',
                'dashboard.context_processors.global_context',

                
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
    # Add other languages here
]

LANGUAGE_CODE = 'ar'

LOCALE_PATHS = [
    BASE_DIR / 'locale',  # Ensure the locale directory is correctly specified
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
