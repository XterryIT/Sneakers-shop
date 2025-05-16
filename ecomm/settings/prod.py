from .base import *
from decouple import config, Csv

DEBUG = False

# берём из переменной в .env, разделённые запятыми
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# пример PostgreSQL, можно любой другой
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# реальный SMTP
EMAIL_BACKEND    = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST       = config('EMAIL_HOST')
EMAIL_PORT       = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS    = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER  = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL   = config('DEFAULT_FROM_EMAIL')

# жёсткие флаги безопасности для HTTPS
CSRF_COOKIE_SECURE       = True
SESSION_COOKIE_SECURE    = True
CSRF_COOKIE_HTTPONLY     = True
SESSION_COOKIE_HTTPONLY  = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER   = True
SECURE_SSL_REDIRECT         = True
