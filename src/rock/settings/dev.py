from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUGdev')

ALLOWED_HOSTS = []

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
