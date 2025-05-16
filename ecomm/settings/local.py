from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# SQLite как в вашем примере
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Почта в консоль, чтобы не отправлять реальные письма
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"