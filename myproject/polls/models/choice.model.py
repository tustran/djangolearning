from django.db import models

class Choice(models.Model):
    question = models.ForeignKey("polls.Question")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        app_label = "polls"