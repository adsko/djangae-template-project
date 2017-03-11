from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return redirect('home')

class Home(TemplateView):
    template_name = 'home/index.html'