# polls/tests/unittest_support.py
import datetime
from django.utils import timezone

from polls.models import Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def delete_all_questions():
    Question.objects.all().delete()