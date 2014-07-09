from django.conf.urls import patterns, url

from quiz import views

urlpatterns = patterns('',
    #url(r'^(?P<quiz_id>\d+)/$', views.main, name='main'),
    url(r'^$', views.main, name='main'),
    url(r'^submit/(?P<quiz_id>\d+)', views.submit, name='submit'),
    url(r'^result/(?P<result_id>\d+)', views.result, name='result'),
    url(r'^twitter/', views.twitter, name='twitter'),    
)
