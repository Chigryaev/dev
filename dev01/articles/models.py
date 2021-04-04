import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from accounts.models import Profile
from storage.models import Storage


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    parent_category = models.ForeignKey(
        "self", blank=True, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.category_name


class Article(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_of_posts",
        blank="True",
        null=True,
    )
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Category, related_name="categories")
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    users_vote = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="post_vote", blank=True
    )
    total_vote = models.PositiveIntegerField(db_index=True, default=0)

    class Meta:
        verbose_name = "Article"
        ordering = ["-datetime"]

    def __str__(self):
        return f"{self.author}, {self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + uuid.uuid4().hex[:4])
        return super(Article, self).save(*args, **kwargs)
