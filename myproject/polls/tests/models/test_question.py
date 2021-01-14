import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

class QuestionMethodTests(TestCase):  # all unittest class need to inherit from TestCase class

    # each test script is defined as a method starting with 'test_'
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        # assert 2 parameters have the same value, if not then the test will fail
        self.assertEqual(future_question.was_published_recently(), False)