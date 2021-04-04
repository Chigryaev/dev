from .models import User, Profile

from rest_framework import status, viewsets, generics, views
from rest_framework.response import Response
from rest_framework import permissions, authentication
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework.parsers import (
    FileUploadParser,
    MultiPartParser,
    FormParser,
    JSONParser,
)


class ProfileViewSetAPI(viewsets.ModelViewSet):
    """
    API for viewing and editing a profile.
    You can also get all subscribers and subscriptions to users by address
    http://127.0.0.1:8000/api/list/?target=username
    Where is the user for whom we want to see subscriptions and subscribers.
    """

    queryset = User.objects.all()
    authentication_classes = (
        # authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    )
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    parser_class = (MultiPartParser, FormParser, JSONParser)
    lookup_field = "username"
