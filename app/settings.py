import os
from pathlib import Path
from typing import Dict

import dj_database_url
from pydantic import ImportString
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Conf(BaseSettings):
    DEBUG: bool = False
    DATABASES: Dict = {"default": dj_database_url.config()}
    INSTALLED_APPS: tuple = ("app",)
    SECRET_KEY: str = "secret"
    LOG_LEVEL: ImportString = "logging.INFO"
    USE_TZ: bool = True
    ROOT_URLCONF: str = "app.urls"
    WSGI_APPLICATION: str = "app.wsgi.application"
    INSTALLED_APPS: tuple = (
        "app",
        "procrastinate.contrib.django",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.staticfiles",
    )
    TEMPLATES: list = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        }
    ]
    MIDDLEWARE: tuple = (
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    )
    STATIC_ROOT: str = ""
    STATIC_URL: str = "/static/"
    STATICFILES_STORAGE: str = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    ALLOWED_HOSTS: list = ["*"]
    LOGGING: Dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "procrastinate": {
                "format": "%(asctime)s %(levelname)-7s %(name)s %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
            "procrastinate": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "procrastinate",
            },
        },
        "loggers": {
            "": {
                "handlers": ["console"],
                "level": "DEBUG",
            },
            "procrastinate": {
                "handlers": ["procrastinate"],
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }


config = Conf()
