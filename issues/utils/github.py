import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Checks if settings are set
required_settings = ('REPO_OWNER', 'REPO_NAME', 'GITHUB_LOGIN', 'GITHUB_ACCESS_TOKEN')
for setting in required_settings:
    if not hasattr(settings, setting) or not getattr(settings, setting):
        raise ImproperlyConfigured('{} must be set and must not be empty'.format(setting))


def create_issue(title, body):
    url = "https://api.github.com/repos/{}/{}/issues".format(settings.REPO_OWNER, settings.REPO_NAME)
    credentials = (settings.GITHUB_LOGIN, settings.GITHUB_ACCESS_TOKEN)
    r = requests.post(url, json={'title': title, 'body': body}, auth=credentials)
    return r
