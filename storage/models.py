from django.db import models
from django.contrib.auth.models import User

from storage.utils import get_upload_filename


def pars_args(*args):
    name, file = args
    return get_upload_filename(file, name)


class Storage(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="upload_files",
        blank="True",
        null=True,
    )
    files = models.ImageField(upload_to=pars_args, blank="True", null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Storage"
        ordering = ["-datetime"]

    def __str__(self):
        return f"{self.user}, {self.files}"