from django.test import TestCase
from issues.forms import IssueForm


class IssueFormTest(TestCase):

    def test_form_validation(self):
        form = IssueForm({'title': 'TestIssue', 'body': None})
        self.assertTrue(form.is_valid())
        form = IssueForm({'title': None, 'body': 'asdf'})
        self.assertFalse(form.is_valid())
