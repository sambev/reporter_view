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


class LoginController(View):
    def post(self, request):
        print request


class SignUpController(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        print request
        user = User()
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponse('User created')
