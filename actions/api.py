from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Tracking
from .serializers import TrackingSerializers
from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets, authentication

from rest_framework.response import Response
from .utils import create_action
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from articles.models import Article


class ActionModelViewSet(viewsets.ModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializers
    authentication_classes = (
        # authentication.TokenAuthentication,
        authentication.BasicAuthentication,
    )
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    """
    GET method with request parameters username for which we are trying to get subscribers.
    Example:
    http://127.0.0.1:8000/api/list/?target=john_doe
    
    """

    def list(self, request, *args, **kwargs):
        target = self.request.query_params.get("target", None)
        self.queryset = self.queryset.filter(
            Q(from_user__username=target) | Q(to_user__username=target)
        )
        return super(ActionModelViewSet, self).list(request, *args, **kwargs)


@api_view(["POST"])
def vote(request):
    """
    Send POST method with post id and action event.
    Example post method body
    {
      "id": 1,
      "action": "vote",
    }
    for url http://127.0.0.1:8000/api/vote/
    """
    json_parser = JSONParser()
    data = json_parser.parse(request)
    article_id = data["id"]
    action = data["action"]
    if article_id and action:
        post = get_object_or_404(Article, id=article_id)
        if action == "vote":
            post.users_vote.add(request.user)
        else:
            post.users_vote.remove(request.user)
        create_action(request.user, action, post)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def tracking(request):

    """Refer to function the vote."""

    json_parser = JSONParser()
    data = json_parser.parse(request)
    user_id = data["id"]
    action = data["action"]
    if user_id and action:
        user = get_object_or_404(User, id=user_id)
        if action == "follow":
            Tracking.objects.get_or_create(from_user=request.user, to_user=user)
        else:
            Tracking.objects.filter(from_user=request.user, to_user=user).delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)