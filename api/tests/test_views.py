from rest_framework import status
from rest_framework.test import APITestCase

from wods.models import Exercise


class ExercisesTestCase(APITestCase):

    def setUp(self):
        super().setUp()
        self.exercise_1 = Exercise.objects.create(name="Pull up")
        self.exercise_2 = Exercise.objects.create(name="Thruster")

    def test_exercises_list(self):
        """Should return the list of all exercises"""
        expected = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": str(self.exercise_1.id),
                    "name": self.exercise_1.name,
                },
                {
                    "id": str(self.exercise_2.id),
                    "name": self.exercise_2.name,
                },
            ],
        }

        response = self.client.get(f"/api/v1/exercises")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)