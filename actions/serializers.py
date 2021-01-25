from rest_framework import serializers
from .models import Tracking
from django.contrib.auth.models import User
from accounts.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("image",)


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "profile",
        ]


class TrackingSerializers(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()

    class Meta:
        model = Tracking
        fields = ["from_user", "to_user"]
