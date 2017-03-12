from django.shortcuts import redirect

# Create your views here.
from django.views.generic import TemplateView
from mixins.auth import LoginRequiredMixin


def index(request):
    return redirect('home')


class Home(TemplateView):
    template_name = 'home/index.html'


class SuccessLoginView(LoginRequiredMixin, TemplateView):
    template_name = 'home/success_login.html'