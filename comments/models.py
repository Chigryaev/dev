from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

from mptt.models import MPTTModel, TreeForeignKey


class Comment(MPTTModel):
    post = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comment_on_posts"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_of_comments"
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    reply_to = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="replyers"
    )
    body = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["-datetime"]

    def __str__(self):
        return self.body[:20]
