from rest_framework import serializers
from .models import Article, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer
from accounts.models import Profile


class ArticleSerializer(serializers.ModelSerializer):

    tags = serializers.SlugRelatedField(
        many=True, queryset=Category.objects.all(), slug_field="category_name"
    )

    author = UserSerializer(read_only=True)
    users_vote = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "author",
            "title",
            "body",
            "tags",
            "slug",
            "datetime",
            "users_vote",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
        read_only_fields = ("slug", "datetime")
        depth = 1
