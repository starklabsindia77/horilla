"""
horilla/horilla_backends.py
"""

import os  # <-- ADD THIS

from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

from horilla import settings


class PrivateMediaStorage(S3Boto3Storage):
    """
    PrivateMediaStorage
    """

    location = os.getenv("NAMESPACE", "private")  # <-- FIXED
    default_acl = "private"
    file_overwrite = False
    custom_domain = False


# To set the private storage globally
models.FileField.storage = PrivateMediaStorage()
models.ImageField.storage = PrivateMediaStorage()
