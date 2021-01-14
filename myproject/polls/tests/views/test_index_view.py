import datetime
import unittest
from django.test import Client
from django.utils import timezone

from polls.models import Question

from polls.tests.unittest_support import create_question, delete_all_questions



class IndexViewTest(unittest.TestCase):

    def setUp(self):
        # Every view test needs a Client
        self.client = Client()
        delete_all_questions()

    def test_index_view_with_no_question(self):
        """
        If no questions exist, the page should still response OK with no questions
        """
        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['questions']), 0)

    def test_index_view_with_less_than_5_recent_questions(self):
        # Create 3 questions
        for i in range(3):
            create_question(question_text="Question %d" % i, days=-i)

        # Issues a GET request
        response = self.client.get('/polls/')

        # Checks that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Checks that the response context contains 5 questions
        self.assertEqual(len(response.context['questions']), 3)

    def test_index_view_with_more_than_5_recent_questions(self):
        # Create 10 questions
        for i in range(10):
            create_question(question_text="Question %d" % i, days=-i)

        # Issues a GET request
        response = self.client.get('/polls/')

        # Checks that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Checks that the response context contains 5 questions
        self.assertEqual(len(response.context['questions']), 5)

    def test_index_view_with_some_future_questions(self):
        # Create 6 questions, from past to future
        # for range -2 to 4, should have 3 future questions
        for i in range(-2, 4):
            create_question(question_text="Question %d" % i, days=i)

        # Issues a GET request
        response = self.client.get('/polls/')

        # Checks that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Checks that the response context contains 3 questions
        self.assertEqual(len(response.context['questions']), 3)
