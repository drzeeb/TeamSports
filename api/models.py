from django.db import models

class Leagues(models.Model):
    leagueName = models.CharField()
    class Meta:
        db_table = "ts_leagues"

class Season(models.Model):
    league: models.ForeignKey(Leagues, on_delete=models.CASCADE)
    year: models.IntegerField(max_length=4)
    class Meta:
        db_table = "ts_seasons"

class Teams(models.Model):
    teamname = models.CharField()
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    city = models.CharField()
    contact = models.CharField()
    phonenumber = models.CharField()
    founded = models.IntegerField()
    class Meta:
        db_table = "ts_teams"

class Players(models.Model):
    firstname = models.CharField()
    lastname = models.CharField()
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    birthday = models.CharField()
    image = models.ImageField(upload_to='player_images')
    class Meta:
        db_table = "ts_players"

class Games(models.Model):
    date: models.DateField
    hometeam: models.ForeignKey(Teams, on_delete=models.CASCADE)
    guestteam: models.ForeignKey(Teams, on_delete=models.CASCADE)
    league: models.ForeignKey(Leagues, on_delete=models.CASCADE)
    class Meta:
        db_table = "ts_games"

class Matches(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    goalsHometeam: models.IntegerField()
    goalsGuestteam: models.IntegerField()
    matchNumber = models.IntegerField()
    startedAt = models.TimeField()
    endedAt = models.TimeField()
    MATCH_TYPE = [
        ("1on1", "1 vs 1"),
        ("2on2", "2 vs 2"),
    ]
    matchType = models.CharField(choices=MATCH_TYPE)
    class Meta:
        db_table = "ts_matches"

class PlayerParticipation(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    class Meta:
        db_table = "ts_player_participation"
