"""
Django settings for horilla project.
"""

import os
from os.path import join
from pathlib import Path

from django.contrib.messages import constants as messages

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY and DEBUG
SECRET_KEY = "django-insecure-j8op9)1q8$1&0^s&p*_0%d#pr@w9qj@1o=3#@d=a(^@9@zd@%j"
DEBUG = True

ALLOWED_HOSTS = ['16.16.48.254', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "notifications",
    "mathfilters",
    "corsheaders",
    "simple_history",
    "django_filters",
    "base",
    "employee",
    "recruitment",
    "leave",
    "pms",
    "onboarding",
    "asset",
    "attendance",
    "payroll",
    "widget_tweaks",
    "django_apscheduler",
]

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "horilla.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "horilla.wsgi.application"

# Database: Force SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Messages
MESSAGE_TAGS = {
    messages.DEBUG: "oh-alert--warning",
    messages.INFO: "oh-alert--info",
    messages.SUCCESS: "oh-alert--success",
    messages.WARNING: "oh-alert--warning",
    messages.ERROR: "oh-alert--danger",
}

# Trusted CSRF Origins
CSRF_TRUSTED_ORIGINS = ['http://16.16.48.254', 'https://16.16.48.254']

LOGIN_URL = "/login"

# History revert setting
SIMPLE_HISTORY_REVERT_DISABLED = True

# Notifications configuration
DJANGO_NOTIFICATIONS_CONFIG = {
    "USE_JSONFIELD": True,
    "SOFT_DELETE": True,
    "USE_WATCHED": True,
    "NOTIFICATIONS_STORAGE": "notifications.storage.DatabaseStorage",
    "TEMPLATE": "notifications.html",
}

# X Frame Options
X_FRAME_OPTIONS = "SAMEORIGIN"

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ("en", "English (US)"),
    ("de", "Deutsche"),
    ("es", "Español"),
    ("fr", "France"),
    ("ar", "عربى"),
    ("pt-br", "Português (Brasil)"),
    ("zh-hans", "Simplified Chinese"),
)

LOCALE_PATHS = [join(BASE_DIR, "horilla", "locale")]

# Production Security settings (ignored in DEBUG mode)
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
