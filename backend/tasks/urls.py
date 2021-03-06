from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, HintViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"hints", HintViewSet, basename="hints")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
