from django.db import models

class Choice(models.Model):
    question = models.ForeignKey("polls.Question",on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


    class Meta:
        app_label = "polls"