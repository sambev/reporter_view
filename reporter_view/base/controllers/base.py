from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.context_processors import csrf

from reporter_view.base.models import User

class BaseController(object):

    @classmethod
    def index(self, request):
        c = {}
        c.update(csrf(request))
        return render(request, 'index.html', c)

    @classmethod
    def home(self, request):
        return render(request, 'home.html')

    @classmethod
    def upload(self, request):
        c = {}
        c.update(csrf(request))
        return render(request, 'upload.html', c)
