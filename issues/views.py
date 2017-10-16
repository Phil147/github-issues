from django.views.generic import TemplateView, FormView
from issues.forms import IssueForm


class IssueCreateView(TemplateView, FormView):
    template_name = 'issues/add_issue.html'
    form_class = IssueForm

    def form_valid(self, form):
        pass
