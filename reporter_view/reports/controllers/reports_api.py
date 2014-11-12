import json

from django.shortcuts import redirect
from django.http import HttpResponse

from reporter_view.reports.services.reports import ReportService

class ReportAPIController(object):

    def __init__(self):
        self.service = ReportService()

    def get_totals(self, request):
        totals = self.service.get_totals(request.user.email)
        return HttpResponse(json.dumps(totals))

    def get_question_summaries(self, request):
        summaries = self.service.get_question_summaries(request.user.email)
        return HttpResponse(json.dumps(summaries))

    def get_context(self, request, question, answer):
        context = self.service.get_context(request.user.email, question, answer)
        return HttpResponse(json.dumps(context))
