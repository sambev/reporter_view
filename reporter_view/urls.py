from django.conf.urls import patterns, include, url
from django.contrib import admin

from reporter_view.base.controllers.base import BaseController
from reporter_view.base.controllers.auth import AuthController
from reporter_view.reports.controllers.reports import ReportController
from reporter_view.reports.controllers.reports_api import ReportAPIController

report_api = ReportAPIController()
report_controller = ReportController()

urlpatterns = patterns('',
    url(r'^$', BaseController.index),
    url(r'^home/', BaseController.home),
    url(r'^upload', BaseController.upload),

    url(r'^login', AuthController.login),
    url(r'^signup', AuthController.signup),

    url(r'^reports/upload', report_controller.upload),
    url(r'^reports/totals', report_api.get_totals),
    url(r'^reports/summary', report_api.get_question_summaries),
    url(r'^reports/context/(?P<question>[\w|\W]+)/(?P<answer>[\w|\W]+)', report_api.get_context)
)
