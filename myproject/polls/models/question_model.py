from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200) # the poll question
    pub_date = models.DateTimeField('date published') # the published date

    class Meta:
        app_label = "polls" # the app this model belong to