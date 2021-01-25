from django.template.defaultfilters import slugify
from django.utils.module_loading import import_string
import inspect
from django.conf import settings
import random
import string
import os
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.storage import default_storage

# import sys
# from django.db import models
# from django.core.files.uploadedfile import InMemoryUploadedFile


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(
        (
            (img_width - crop_width) // 2,
            (img_height - crop_height) // 2,
            (img_width + crop_width) // 2,
            (img_height + crop_height) // 2,
        )
    )


def compress_image(image):
    image_temproary = Image.open(image)
    image_temproary = crop_center(image_temproary, 960, 360)
    output_io_stream = BytesIO()
    image_temproary = image_temproary.convert("RGB")
    image_temproary.save(
        output_io_stream, format="JPEG", quality=75,
    )
    output_io_stream.seek(0)
    image = File(output_io_stream, name=image.name)
    return image


def get_upload_filename(upload_name, request):
    user_path = get_user_path(request.user)
    date_path = datetime.now().strftime("%Y/%m/%d")
    upload_path = os.path.join(settings.STORAGE_UPLOAD_PATH, user_path, date_path)
    upload_name = slugify_filename(str(upload_name))
    return storage.get_available_name(os.path.join(upload_path, upload_name))


def get_user_path(user):
    user_path = ""
    if user:
        user_path = user
    else:
        user_path = "Anonymous_" + get_random_string()
    return str(user_path)


def slugify_filename(filename):
    name, ext = os.path.splitext(filename)
    slugified = get_slugified_name(name)
    return slugified + ext


def get_slugified_name(filename):
    # slugified = slugify(filename)
    # return slugified or get_random_string()
    return get_random_string()


def get_media_url(path):
    return storage.url(path)


def get_random_string():
    return "".join(random.sample(string.ascii_lowercase * 16, 16))


def get_storage_class():
    return import_string(
        getattr(settings, "STORAGE", "django.core.files.storage.DefaultStorage",)
    )()


storage = get_storage_class()
