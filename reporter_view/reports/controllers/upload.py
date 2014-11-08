import json

from django.views.generic import View
from django.shortcuts import redirect

from reporter_view.reports.services.reports import ReportService

class ReportUploadController(View):

    def __init__(self):
        self.service = ReportService()

    def post(self, request):
        reports = json.loads(request.FILES['reports'].read())
        self.service.make_new_db(request.user.email, reports)
        return redirect('/home')

