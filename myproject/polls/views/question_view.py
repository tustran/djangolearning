from django.template.response import TemplateResponse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.urls import reverse
from django.shortcuts import get_object_or_404

from polls.models import Question, Choice

class QuestionView(View):

    template = "polls/question.html"

    def get(self, request, question_id=None):
        context = {}
        context['question'] = get_object_or_404(Question, pk=question_id)
        return TemplateResponse(request, self.template, context)
    
    # It's better to create another [FormView](https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/) instead of sharing the same view for Get and Post
    def post(self, request, question_id = None):
        choice = get_object_or_404(Choice, pk=request.POST.get("poll_choice", None))
        choice.votes += 1 # increase vote
        choice.save()

        return HttpResponseRedirect(reverse("poll_result", kwargs={"question_id": choice.question_id}))