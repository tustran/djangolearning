# from django.template.response import TemplateResponse
# from django.views.generic.base import View


# class IndexView(View):

#     template = "polls/index.html"

#     def get(self, request):
#         context = {}
#         context['var_string'] = "This Is A String" # a string
#         context['var_array'] = ["This", "Is", "An", "Array", ]  # an array of string
#         context['var_dict'] = {
#                             "part1": "This",
#                             "part2": "Is",
#                             "part3": "A",
#                             "part4": "Dict",
#                         }  # a dictionary (dict)
#         return TemplateResponse(request, self.template, context)

#######################################################################################

# from django.template.response import TemplateResponse
# from django.views.generic.base import TemplateView

# from polls.models import Question

# class IndexView(TemplateView):

#     template_name = "polls/index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['questions'] = Question.objects.all()
#         return context

#########################################################################################

from django.template.response import TemplateResponse
from django.views.generic.base import View
from django.utils import timezone

from polls.models import Question


class IndexView(View):

    template = "polls/index.html"

    def get(self, request):
        context = {}
        """
        Returns the recent 5 questions published, not including those set
        to be in the future
        """
        # context['questions'] = Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by("-pub_date")[:5]

        context['today_questions'] = Question.objects.published_recently().order_by("-pub_date")[:5]

        return TemplateResponse(request, self.template, context)