from django.conf.urls import patterns, url

from quiz import views

urlpatterns = patterns('',
    url(r'^(?P<quiz_id>\d+)/$', views.main, name='main'),
    url(r'^(?P<quiz_id>\d+)/submit/$', views.submit, name='submit'),
    url(r'^(?P<quiz_id>\d+)/result/$', views.result, name='result'),
)
