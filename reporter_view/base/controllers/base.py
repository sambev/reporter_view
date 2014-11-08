from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.context_processors import csrf

from reporter_view.base.models import User

class BaseController(View):

    def get(self, request):
        c = {}
        c.update(csrf(request))
        return render(request, 'index.html', c)


class HomeController(View):

    def get(self, request):
        c = {}
        c.update(csrf(request))
        return render(request, 'home.html', c)
