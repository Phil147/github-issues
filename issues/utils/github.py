import requests
from django.conf import settings


def create_issue(title, body):
    url = "https://api.github.com/repos/{}/{}/issues".format(settings.REPO_OWNER, settings.REPO_NAME)
    credentials = (settings.GITHUB_LOGIN, settings.GITHUB_ACCESS_TOKEN)
    r = requests.post(url, json={'title': title, 'body': body}, auth=credentials)
    return r
