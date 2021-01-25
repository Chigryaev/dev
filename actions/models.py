from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib import auth


class Action(models.Model):
    user = models.ForeignKey(
        User,
        related_name="actions",
        db_index=True,
        on_delete=models.CASCADE,
    )
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="target_obj",
        on_delete=models.CASCADE,
    )
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey("target_ct", "target_id")
    datetime = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-datetime",)
        verbose_name = "Action"


class Tracking(models.Model):
    from_user = models.ForeignKey(
        User, related_name="following_links", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name="follower_links", on_delete=models.CASCADE
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        if self.from_user == self.to_user:
            raise ValueError("Cannot follow yourself.")
        super(Tracking, self).save(**kwargs)

    class Meta:
        unique_together = (("to_user", "from_user"),)
        verbose_name = "Tracking"

    def __str__(self):
        return f"{self.from_user}, {self.to_user}"