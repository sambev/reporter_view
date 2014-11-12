from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

from reporter_view.base.models import User

class AuthController(object):

    @classmethod
    def login(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return redirect('/upload')
        else:
            return redirect('/')

    @classmethod
    def signup(self, request):
        user = User()
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.save()

        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user:
            login(request, user)

        return redirect('/upload')

    @classmethod
    def signout(self, request):
        logout(request)
        return redirect('/')


    @classmethod
    def alpha_request(self, request):
        send_mail(
            'Alpha Invite Request', # Subject
            'This person wants an invite', # Message
            request.POST.get('alpha_email', None), # From email
            [settings.DEFAULT_TO_EMAIL]
        )
