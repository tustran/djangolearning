from django.template.response import TemplateResponse
from django.views.generic.base import View


class IndexView(View):

    template = "polls/index.html"

    def get(self, request):
        context = {}
        context['var_string'] = "This Is A String" # a string
        context['var_array'] = ["This", "Is", "An", "Array", ]  # an array of string
        context['var_dict'] = {
                            "part1": "This",
                            "part2": "Is",
                            "part3": "A",
                            "part4": "Dict",
                        }  # a dictionary (dict)
        return TemplateResponse(request, self.template, context)