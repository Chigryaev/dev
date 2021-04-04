from rest_framework import serializers
from .models import Storage
from accounts.models import User


class StorageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = ("url", "files", "user_id")


class DeleteFromStorageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = ("url", "files")
