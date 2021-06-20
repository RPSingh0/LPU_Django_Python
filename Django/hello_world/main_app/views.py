from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# class based views


# def home_page(request):
#     context = {"name": "rupinder", "languages": ["python", "c++"]}
#     return render(request, "main_app/index.html", context)

class home_page(TemplateView):
    template_name = "main_app/index.html"

# def table_page(request):
#     context = {}
#     return render(request, "main_app/table.html", context)
