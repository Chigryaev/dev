from django.urls import path, include
from .api import ActionModelViewSet, tracking, vote
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("vote/", vote, name="vote"),
    path("follow/", tracking, name="follow"),
    path(
        "list/",
        ActionModelViewSet.as_view({"get": "list"}),
        name="list",
    ),
]
