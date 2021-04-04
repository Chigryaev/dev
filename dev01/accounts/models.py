from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericRelation

from rest_framework.authtoken.models import Token

from storage.utils import get_upload_filename


def pars_args(*args):
    name, file = args
    return get_upload_filename(file, name)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=pars_args, blank="True", null=True)

    class Meta:
        verbose_name = "Profile"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username
