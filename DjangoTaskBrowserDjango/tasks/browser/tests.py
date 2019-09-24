import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Task


class QuestionModelTests(TestCase):

    def test_was_scheduled_far_in_the_future(self):
        """
        was_recently_started() returns False for tasks whose start_date
        is far in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_task = Task(start_date=time)
        self.assertIs(future_task.was_recently_started(), False)
