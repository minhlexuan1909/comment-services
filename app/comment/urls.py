"""
URL mappings for the comment app
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet

router = DefaultRouter()
router.register("comment", CommentViewSet)

app_name = "comment"

urlpatterns = [
    path("", include(router.urls)),
]
