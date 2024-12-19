"""Define URLs Pattern for learning_logs."""

from django.urls import re_path
from . import views

app_name="learning"

urlpatterns=[
    #Home Page
    re_path('^$',views.index,name='index'),
    
    re_path(r'^topics/$',views.topics,name='topics'),

    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]