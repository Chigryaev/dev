from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from accounts.serializers import UserSerializer
from articles.models import Article


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "post",
            "id",
            "body",
            "user",
            "datetime",
            "parent",
            "reply_to",
        ]

        read_only_fields = ["user"]

    def create(self, validated_data):
        return Comment.objects.create(
            post=validated_data.get("post"),
            body=validated_data.get("body"),
            parent=validated_data.get("parent"),
            reply_to=validated_data.get("reply_to"),
            user=validated_data.get("user"),
        )
