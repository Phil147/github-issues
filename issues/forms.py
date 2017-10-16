from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import Form, CharField


class IssueForm(Form):
    title = CharField(required=True, max_length=255)
    body = CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'issue-create-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Create Issue'))
