import logging
import os

import django

from app import settings

# expose attributes to module scope to maintain django compatibility
for setting in settings.config.dict().items():
    setattr(settings, *setting)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()
logging.basicConfig(level=settings.config.LOG_LEVEL)
