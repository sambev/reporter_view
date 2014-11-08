from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login

from reporter_view.base.models import User

class LoginController(View):

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('/')


class SignUpController(View):

    def get(self, request):
        return redirect('/')

    def post(self, request):
        user = User()
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.save()
        login(request, user)

        return render(request, 'home.html')
