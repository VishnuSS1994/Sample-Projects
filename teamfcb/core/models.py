from django.db import models


# Create your models here.
class Team(models.Model):
    """Model for creating teams"""

    team_name = models.CharField(max_length=16)
    team_members = models.CharField(max_length=512)
    coach = models.CharField(max_length=32)
    managers = models.CharField(max_length=256)

    def __str__(self):
        return self.coach


class MatchSchedule(models.Model):
    """Models for schedule team matches"""

    match_teams = models.CharField(max_length=32)
    start_time = models.CharField(max_length=24)
    end_time = models.CharField(max_length=24)
    venue = models.CharField(max_length=16)

    def __str__(self):
        return self.match_teams
