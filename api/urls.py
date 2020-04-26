from rest_framework import routers
from django.urls import path, include

from api import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"exercises", views.ExerciseViewSet)


urlpatterns = [
    # keep this at the bottom
    path("", include(router.urls)),
]
