from django.conf.urls import url

from . import views

app_name = 'backlog'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
]