from django.urls import path, include
from rest_framework import routers
from .api import DeleteFromStorageAPIView, StorageList, UploadModelViewSet

router = routers.DefaultRouter()
router.register(r"storage", UploadModelViewSet, basename="storage")

urlpatterns = [
    path("storage/<int:pk>/delete/", DeleteFromStorageAPIView.as_view()),
    path("storage/list/", StorageList.as_view()),
    path("", include(router.urls)),
]
