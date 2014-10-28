from django.conf.urls import patterns, include, url
from django.contrib import admin
from reporter_view.base.controllers.base import BaseController, \
    LoginController, SignUpController

urlpatterns = patterns('',
    url(r'^$', BaseController.as_view()),
    url(r'^login', LoginController.as_view()),
    url(r'^signup', SignUpController.as_view())
)
