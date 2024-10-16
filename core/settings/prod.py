from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv("DB_HOST"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'PORT': os.getenv("DB_PORT"),
}
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
