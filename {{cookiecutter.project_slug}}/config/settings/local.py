from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1",
                 '10.0.2.2',    # Virtualbox
                 '10.0.3.2',    # Genymotion
                 ]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "KEY_PREFIX": "",
        "VERSION": '1',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                'max_connections': 50,      # Local use only
            }
        }
    }
}

# EMAIL
# ------------------------------------------------------------------------------
{% if cookiecutter.use_mailhog == 'y' and cookiecutter.use_docker == 'y' -%}
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = 1025
{%- elif cookiecutter.use_mailhog == 'y' and cookiecutter.use_docker == 'n' -%}
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
{%- else -%}
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
{%- endif %}

{%- if cookiecutter.use_whitenoise == 'y' %}

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405
{% endif %}

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2", "10.0.3.2"]
{% if cookiecutter.use_docker == 'y' -%}
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
{%- endif %}

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405
{% if cookiecutter.use_celery == 'y' -%}

# Celery
# ------------------------------------------------------------------------------
{% if cookiecutter.use_docker == 'n' -%}
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-always-eager
CELERY_TASK_ALWAYS_EAGER = True
{%- endif %}
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True

{%- endif %}



# Your stuff...
# ------------------------------------------------------------------------------
SKIP_CACHE = env.bool('SKIP_CACHE', default=True)