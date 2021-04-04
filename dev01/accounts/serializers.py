from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from storage.serializers import StorageSerializers

from actions.serializers import TrackingSerializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("image", "description")


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "profile",
        ]
        lookup_field = "username"
        extra_kwargs = {"url": {"lookup_field": "username"}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile")
        profile = instance.profile

        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()

        profile.description = profile_data.get("description", profile.bio)
        profile.image = profile_data.get("image", profile.image)
        profile.save()

        return instance
