import json

from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from reporter_view.reports.services.reports import ReportService

class ReportAPIController(object):

    def __init__(self):
        self.service = ReportService()

    @method_decorator(login_required)
    def get_totals(self, request):
        totals = self.service.get_totals(request.user.email)
        return HttpResponse(json.dumps(totals))

    @method_decorator(login_required)
    def get_question_summaries(self, request):
        summaries = self.service.get_question_summaries(request.user.email)
        return HttpResponse(json.dumps(summaries))

    @method_decorator(login_required)
    def get_context(self, request, question, answer):
        context = self.service.get_context(request.user.email, question, answer)
        return HttpResponse(json.dumps(context))
