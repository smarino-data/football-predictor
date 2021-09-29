from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Results(models.Model):
    match_date = models.DateField()
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)
    fthg = models.IntegerField()
    ftag = models.IntegerField()
    ftr = models.CharField(max_length=1)

class Team(models.Model):
    team = models.CharField(max_length=200)
    league = models.CharField(max_length=200)
    attack = models.IntegerField()
    midfield = models.IntegerField()
    defence = models.IntegerField()
    overall = models.IntegerField()
    submitted_date = models.DateField()

class Fixtures(models.Model):
    match_date = models.DateField()
    competition = models.CharField(max_length=200)
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)


