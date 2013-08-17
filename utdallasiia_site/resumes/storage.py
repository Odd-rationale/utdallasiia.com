from django.conf import settings
from django.core.files.storage import FileSystemStorage

smedia_storage = FileSystemStorage(
    location=settings.SMEDIA_ROOT,
    base_url=settings.SMEDIA_URL,
)
