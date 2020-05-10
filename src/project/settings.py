# import os
from os import getenv
from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import dj_database_url
from django.urls import reverse_lazy
from dynaconf import settings as _settings

PROJECT_DIR = Path(__file__).parent.resolve()
BASE_DIR = PROJECT_DIR.parent.resolve()
REPO_DIR = BASE_DIR.parent.resolve()


SECRET_KEY = _settings.SECRET_KEY

DEBUG = _settings.DEBUG
PROFILING = _settings.PROFILING

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS + ["localhost", "127.0.0.1", "0.0.0.0"]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    # "silk", #убрать перед тестами
    "django.contrib.staticfiles",
    "apps.onboarding.apps.OnboardingConfig",
    "apps.index.apps.IndexConfig",
    "apps.resume",
    "apps.thoughts.apps.ThoughtsConfig",
    "apps.blog.apps.BlogConfig",
]

# if PROFILING:
#   INSTALLED_APPS.append("silk")


MIDDLEWARE = [
    # "silk.middleware.SilkyMiddleware",#убрать перед тестами
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]

if PROFILING:
    # MIDDLEWARE=["silk.middleware.SilkyMiddleware"]+MIDDLEWARE
    SILKY_PYTHON_PROFILER = True
    SILKY_PYTHON_PROFILER_BINARY = True


ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [PROJECT_DIR / "jinja2",],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "project.jinja2.environment",
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates",],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {"project_tags": "project.templatetags",},
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

_db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    _db_url = getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.parse(_db_url, conn_max_age=600),
    # {
    #'ENGINE': 'django.db.backends.sqlite3',
    #'NAME': (BASE_DIR / 'db.sqlite3').as_posix(), #
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

"""PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]"""

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"
LOCAL_TIME_ZONE = _settings.LOCAL_TIME_ZONE

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/assets/"  #'/static/'  это не папка а ссылка
# STATIC_URL = '/static/'  путь от которого отсчит путь к статич файлам

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

STATIC_ROOT = REPO_DIR / ".static"  # место где хранится статика

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

if not DEBUG:

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=_settings.SENTRY_DSN,
        integrations=[DjangoIntegration()],
        send_default_pii=True,
    )

LOGIN_URL = reverse_lazy("onboarding:sign_in")
LOGIN_REDIRECT_URL = reverse_lazy("onboarding:me")

SITE_ID = _settings.SITE_ID

EMAIL_HOST = _settings.EMAIL_HOST
EMAIL_HOST_PASSWORD = _settings.EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = _settings.EMAIL_HOST_USER
EMAIL_PORT = _settings.EMAIL_PORT
EMAIL_USE_SSL = _settings.EMAIL_USE_SSL
EMAIL_USE_TLS = _settings.EMAIL_USE_TLS

EMAIL_FROM = _settings.EMAIL_FROM
