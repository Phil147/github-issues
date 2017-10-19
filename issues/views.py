from django.views.generic import TemplateView, FormView
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy

from issues.forms import IssueForm
from issues.utils.github import create_issue


class IssueCreateView(TemplateView, FormView):
    template_name = 'issues/add_issue.html'
    form_class = IssueForm
    success_url = reverse_lazy('add-issue')

    def form_valid(self, form):
        r = create_issue(form.cleaned_data['title'], form.cleaned_data['body'])
        response = r.json()
        if r.status_code != 201:
            message = 'Oops something went wrong, error message: {}'.format(response['message'])
            message_level = messages.ERROR
        else:
            message = mark_safe(
                'Issue #{} created. Have a look <a href="{}">here</a>'.format(response['number'], response['html_url']))
            message_level = messages.SUCCESS
        messages.add_message(self.request, message_level, message)
        return super().form_valid(form)
