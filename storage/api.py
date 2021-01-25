from rest_framework.exceptions import ParseError
from rest_framework.parsers import (
    FileUploadParser,
    MultiPartParser,
    FormParser,
    JSONParser,
)
from django.core.files.storage import default_storage
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework import permissions, authentication
from .utils import get_upload_filename, get_media_url, compress_image
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from .serializers import StorageSerializers, DeleteFromStorageSerializers
from .models import Storage


class UploadModelViewSet(viewsets.ModelViewSet):
    pass


class DeleteFromStorageAPIView(generics.DestroyAPIView):
    """
    API for deleting files on the server
    Url for DELETE http://127.0.0.1:8000/api/storage/<id>/delete/
    """

    queryset = Storage.objects.all()
    serializer_class = DeleteFromStorageSerializers
    authentication_classes = [
        # authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    ]


class StorageList(generics.ListCreateAPIView):
    """
    Storage List allows you to upload user files to the server, as well as view them
    Url for upload http://127.0.0.1:8000/api/storage/list/
    """

    parser_class = (MultiPartParser, FormParser, JSONParser)
    queryset = Storage.objects.all()
    serializer_class = StorageSerializers
    authentication_classes = [
        # authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user_id=self.request.user.id)

    def list(self, request):
        query = self.queryset.filter(user_id=self.request.user)
        serializer = self.get_serializer(
            query,
            context={
                "request": request,
            },
            many=True,
        )
        return Response(serializer.data)