from django.conf.urls import patterns, include, url
from django.contrib import admin

from reporter_view.base.controllers.base import BaseController, HomeController
from reporter_view.base.controllers.auth import LoginController, SignUpController
from reporter_view.reports.controllers.upload import ReportUploadController

urlpatterns = patterns('',
    url(r'^$', BaseController.as_view()),
    url(r'^login', LoginController.as_view()),
    url(r'^signup', SignUpController.as_view()),
    url(r'^home', HomeController.as_view()),
    url(r'^reports/upload', ReportUploadController.as_view()),
)
