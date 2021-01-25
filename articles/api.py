from rest_framework import viewsets
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
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Article


class ArticleModelViewSet(viewsets.ModelViewSet):
    """
    ArticleModelViewSet allows you to create, update, and view articles.
    In order to receive comments on the article. It is required to send a GET request for url
    http://127.0.0.1:8000/api/comment/id/
    where id is the article number.
    In order to upload files to the article, send them to the address http://127.0.0.1:8000/api/storage/list/
    """

    queryset = Article.objects.all()
    authentication_classes = (
        # authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    )
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    parser_class = (JSONParser, MultiPartParser, FormParser)
    serializer_class = ArticleSerializer
    lookup_field = "slug"

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
