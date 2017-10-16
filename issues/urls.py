from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IssueCreateView.as_view(), name='add-issue'),
]