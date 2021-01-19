import datetime
from django.utils import timezone
from django.db import models

class QuestionManager(models.Manager):

    def published_recently(self):
        exclude_list = []
        for question in Question.objects.all():
            if not question.was_published_recently():
                exclude_list.append(question.id)

        return Question.objects.all().exclude(id__in=exclude_list)

class Question(models.Model):
    question_text = models.CharField(max_length=200) # the poll question
    pub_date = models.DateTimeField('date published') # the published date

    objects = QuestionManager()

    class Meta:
        app_label = "polls" # the app this model belong to

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    