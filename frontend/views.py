from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response

class Frontend(TemplateView):

    def get(self, request):
        return render_to_response("index.html")