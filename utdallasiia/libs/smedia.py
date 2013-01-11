from django.core.files.storage import FileSystemStorage
from django.conf import settings

smedia_storage = FileSystemStorage(location=settings.SMEDIA_ROOT, base_url=settings.SMEDIA_URL)