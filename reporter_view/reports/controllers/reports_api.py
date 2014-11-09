import json

from django.shortcuts import redirect
from django.http import HttpResponse

from reporter_view.reports.services.reports import ReportService

class ReportAPIController(object):

    def __init__(self):
        self.service = ReportService()

    def get_totals(self, request):
        totals = self.service.get_totals(request.user.email)
        print totals
        return HttpResponse(json.dumps(totals))

