import unittest
from django.test import Client

class IndexViewTest(unittest.TestCase):
    def setUp(self):
        # Every view test needs a client.
        self.client = Client()

    def test_index_view(self):
        # Issues a GET request.
        response = self.client.get('/polls/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 questions.
        self.assertEqual(len(response.context['questions']), 5)