from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.views.generic import ListView
from .models import *
# Create your views here.


class Login(LoginView):
    """Serves login page."""

    template_name = 'login.html'


class Logout(LogoutView):
    """Serves login page."""

    template_name = 'logout.html'


class Team(CreateView):
    """View for teams"""

    model = Team
    fields = ['team_name', 'team_members', 'coach', 'managers']
    template_name = 'team.html'
    success_url = '/core/team_list/'

    def clean(self, *args, **kwargs):
        if Team.objects.all().count() == 10:
            raise ValidationError("Team registration completed")


class TeamList(ListView):
    model = Team
    template_name = 'team_list.html'
    context_object_name = 'teams'
    allow_empty = True


class StartMatch(generic.TemplateView):

    template_name = 'start_match.html'
    success_url = '/core/match_create/'


class MatchCreate(CreateView):
    model = MatchSchedule
    fields = ['match_teams', 'start_time', 'end_time', 'venue']
    template_name = 'match.html'
    success_url = '/core/matchcreated_list/'


class MatchCreated(ListView):
    model = MatchSchedule
    template_name = 'matchcreated_list.html'
    context_object_name = 'match'
    allow_empty = True
