from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.questions_list, name='questions_list'),
    url('^(?P<pk>\d+)/$', views.questions_detail, name='questions_detail'),
    url('^new/$', views.questions_new, name='questions_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.questions_edit, name='questions_edit'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_questions, name='add_comment_to_questions'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]