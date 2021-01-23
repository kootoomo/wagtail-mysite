from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '03sxzutqh7^x%q*0w174lm=7&k50zanl(or(!rf61rxe$ky&n-'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    # 'debug_toolbar',
    'django_extensions',
    'wagtail.contrib.styleguide',
]

MIDDLEWARE = MIDDLEWARE + [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
#        "LOCATION": "D:\devel\wagtail\mysite\cache"
	"LOCATION": "../cache"
    }
}

try:
    from .local import *
except ImportError:
    pass
