from rest_framework import serializers

from wods.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ("id", "name")