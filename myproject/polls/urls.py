from django.urls import include, re_path, path
from polls.views.index_view import IndexView
from polls.views.question_view import QuestionView

urlpatterns = (
    path('', IndexView.as_view(), name="index"),
    re_path(r'^(?P<question_id>\d+)$', QuestionView.as_view(), name="poll_detail"),
    re_path(r'^(?P<question_id>\d+)/result$', QuestionView.as_view(template="polls/result.html"), name="poll_result"), # using same view but different template
)