import os
import dj_database_url

# Secret Key (secure it with an environment variable)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-t8qx^x@-n#pr=cgg)nx&m0%r7$$)k$0k7df(2xb5hvb-)(ygtu')

# Debug should be False in production
DEBUG = False

# Allow all hosts temporarily (we’ll refine this later)
ALLOWED_HOSTS = ['*']

# CSRF Trusted Origins (update after deployment with your domain)
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')

# Database configuration using Railway’s DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Static files with Whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core/static']
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (optional, refine later if needed)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'