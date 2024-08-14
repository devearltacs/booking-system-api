import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Event


# Create your tests here.
class EventModelTests(TestCase):
    def test_was_published_recently_with_future_event(self):
        """
        was_published_recently() returns False for events whose date_created
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(date_created=time)
        self.assertIs(future_event.was_published_recently(), False)
        
    def test_was_published_recently_with_old_event(self):
        """
        was_published_recently() returns False for events whose date_created
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_event = Event(date_created=time)
        self.assertIs(old_event.was_published_recently(), False)


    def test_was_published_recently_with_recent_event(self):
        """
        was_published_recently() returns True for events whose date_created
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_event = Event(date_created=time)
        self.assertIs(recent_event.was_published_recently(), True)