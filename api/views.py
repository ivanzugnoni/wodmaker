from django.shortcuts import render
from rest_framework import viewsets, mixins

from wods.models import Exercise
from api.serializers import ExerciseSerializer


class ExerciseViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer