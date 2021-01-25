from rest_framework.routers import DefaultRouter
from .api import CommentModelViewSet


router = DefaultRouter()
router.register(r"comment", CommentModelViewSet, basename="comment")
urlpatterns = router.urls