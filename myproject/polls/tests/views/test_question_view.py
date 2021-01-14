import datetime
import unittest
from django.urls import reverse
from django.test import Client
from django.utils import timezone

from polls.models import Question

from polls.tests.unittest_support import create_question, delete_all_questions


class QuestionViewTest(unittest.TestCase):

    def setUp(self):
        # Every view test needs a Client
        self.client = Client()
        delete_all_questions()

    def test_get_valid_question(self):
        """
        Get a valid question should response OK
        """
        valid_question = create_question(question_text='Valid question',
                                         days=0)
        response = self.client.get(reverse('poll_detail',
                                           args=(valid_question.id,)))
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_question(self):
        """
        Get an invalid question should response 404 NOT FOUND
        """
        invalid_question_id = 404
        response = self.client.get(reverse('poll_detail',
                                           args=(invalid_question_id,)))
        self.assertEqual(response.status_code, 404)