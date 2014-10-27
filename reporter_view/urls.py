from django.conf.urls import patterns, include, url
from django.contrib import admin
from reporter_view.base.controllers.base import index, login, sign_up

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login', login),
    url(r'^signup', sign_up)
)
