import nflgame
from orm import *

def fetch_data(year):
  save_data(query_data(year))
  

def query_data(year):
  return nflgame.games(year)

def save_data(games):
  for game in games:
    home = game.home
    away = game.away
    home_team, created = Team.get_or_create(name=home)
    away_team, created = Team.get_or_create(name=away)
    year = game.schedule['year']
    week = game.schedule['week']
    Game.get_or_create(
      gamekey=game.gamekey,
      home_team=home_team,
      away_team=away_team,
      home_score=game.score_home,
      away_score=game.score_away,
      year=year,
      week=week,
    )