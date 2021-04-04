from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from django.views.generic import TemplateView

from .api import ProfileViewSetAPI
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"profile", ProfileViewSetAPI, basename="profile")

urlpatterns = router.urls
