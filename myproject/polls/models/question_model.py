import datetime
from django.utils import timezone
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200) # the poll question
    pub_date = models.DateTimeField('date published') # the published date

    class Meta:
        app_label = "polls" # the app this model belong to

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    