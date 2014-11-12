import json

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from reporter_view.reports.services.reports import ReportService

class ReportController(object):

    def __init__(self):
        self.service = ReportService()

    @method_decorator(login_required)
    def upload(self, request):
        reports = json.loads(request.FILES['reports'].read())
        self.service.make_new_db(request.user.email, reports)
        return redirect('/home')

