from django.urls import include, re_path
from polls.views.index_view import IndexView

urlpatterns = [
    re_path(r'^$', IndexView.as_view()),
]