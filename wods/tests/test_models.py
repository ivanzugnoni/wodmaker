from django.test import TestCase

from wods.models import Exercise


class ExerciseModelTestCase(TestCase):

    def setUp(self):
        pass

    def test_exercise(self):
        # preconditions
        self.assertEqual(Exercise.objects.count(), 0)

        Exercise.objects.create(name="Thruster")

        # postconditions
        self.assertEqual(Exercise.objects.count(), 1) 