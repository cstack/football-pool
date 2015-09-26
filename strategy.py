from orm import *

class Strategy:
  def predict(self, game):
    raise Exception('Subclass must implement predict')

  def record(self, team, games):
    home_games = games.select().where(Game.home_team == team)
    away_games = games.select().where(Game.away_team == team)
    total = home_games.count() + away_games.count()
    if total == 0:
      return 0
    home_wins = home_games.select().where(Game.home_score > Game.away_score)
    away_wins = away_games.select().where(Game.away_score > Game.home_score)
    wins = home_wins.count() + away_wins.count()
    return float(wins) / total

class Alphabetical(Strategy):
  def predict(self, game):
    if game.home_team.name < game.away_team.name:
      return game.home_team
    else:
      return game.away_team

class HomeTeam(Strategy):
  def predict(self, game):
    return game.home_team

class AllTimeRecord(Strategy):
  def predict(self, game):
    previous_games = game.previous_games()
    home_record = self.record(game.home_team, previous_games)
    away_record = self.record(game.away_team, previous_games)
    if home_record > away_record:
      return game.home_team
    return game.away_team

class RecordThisYear(Strategy):
  def predict(self, game):
    previous_games = game.previous_games().where(Game.year == game.year)
    home_record = self.record(game.home_team, previous_games)
    away_record = self.record(game.away_team, previous_games)
    if home_record > away_record:
      return game.home_team
    return game.away_team

strategies = [
  Alphabetical,
  HomeTeam,
  AllTimeRecord,
  RecordThisYear,
]