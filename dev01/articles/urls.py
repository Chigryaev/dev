from django.conf import settings
from django.urls import path, include


from rest_framework.routers import DefaultRouter
from .api import ArticleModelViewSet


router = DefaultRouter()
router.register(r"article", ArticleModelViewSet, basename="article")
urlpatterns = router.urls
