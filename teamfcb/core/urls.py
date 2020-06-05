from django.conf.urls import url
from . import views
from .models import *

app_name = 'core'

urlpatterns = [

    url(r'^login/$', views.Login.as_view(), name='login'),

    url(r'^teams/$', views.Team.as_view(), name='teams'),

    url(r'^team_list/$', views.TeamList.as_view(model=Team), name='team_list'),

    url(r'^start_match/$', views.StartMatch.as_view(), name='start_match'),

    url(r'^match_create/$', views.MatchCreate.as_view(), name='match_create'),

    url(r'^matchcreated_list/$', views.MatchCreated.as_view(), name='match_created'),

    url(r'^logout/$', views.Logout.as_view(), name='logout'),

]
