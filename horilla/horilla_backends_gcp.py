"""
horilla/horilla_backends_gcp.py
"""

import os  # <--- Add this line

from django.db import models
from storages.backends.gcloud import GoogleCloudStorage

from horilla import settings


class PrivateMediaStorage(GoogleCloudStorage):
    """
    PrivateMediaStorage
    """

    location = os.getenv("NAMESPACE", "private")  # <-- Replace settings.env with os.getenv
    default_acl = "private"
    file_overwrite = False


# To set the private storage globally
models.FileField.storage = PrivateMediaStorage()
models.ImageField.storage = PrivateMediaStorage()
