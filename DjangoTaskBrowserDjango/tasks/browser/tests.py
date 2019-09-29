import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Task


class QuestionModelTests(TestCase):

    def test_was_scheduled_far_in_the_future(self):
        """
        was_recently_started() returns False for questions whose start_date
        is far in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_task = Task(start_date=time)
        self.assertIs(future_task.was_recently_started(), False)
    def test_was_start_date_greater_end_date_duration(self):
        """
        taskduration() should return Error
        if start date is greater than end date.
        """
        start_date = timezone.now() + datetime.timedelta(days=30)
        end_date = timezone.now()
        checking_task = Task(start_date=start_date, end_date=end_date)
        self.assertIs(checking_task.taskduration(checking_task), "Error")