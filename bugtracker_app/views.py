import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from bugtracker_app.models import IssueForm
from bugtracker_app.models import Setting

from . import mail_parser

APP_NAME = 'bugtracker'
setting = Setting.load()

class ReportIssue(TemplateView):
    template_name = APP_NAME+'/report_issue.html'
    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            r = requests.post(
                setting.redmine_url+'/issues.json',
                json={
                    'issue': {
                        "project_id": 'the_matrix',
                        "subject": issue.title,
                        "description": issue.body,
                        "priority_id": 4,
                    }
                },
                params={'key':setting.redmine_api_access_key})
            return self.get(request)
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = IssueForm()
        return ctx

class NewMessagesList(ListView):
    template_name = APP_NAME+'/new_messages_list.html'

    def get_queryset(self):
        return mail_parser.get_unread_messages()

    def get_context_data(self, **kwargs):
    	ctx = super().get_context_data(**kwargs)
    	ctx['issue_list'] = mail_parser.parse_messages(mail_parser.get_unread_messages())
    	return ctx