from django.shortcuts import render
# Import Django generic library, import Template View from views.generic
# from django.views import generic
from django.views.generic import TemplateView
# Import Booking & User models from .models
# from .models import Booking, UserReg


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html',)
