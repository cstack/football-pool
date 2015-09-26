from peewee import *

db = SqliteDatabase('data/data.db')

def create_tables():
  db.connect()
  db.create_tables([Team, Game])

class Team(Model):
  name = CharField()

  class Meta:
    database = db

class Game(Model):
  home_team = ForeignKeyField(Team, related_name='home_team')
  away_team = ForeignKeyField(Team, related_name='away_team')
  home_score = IntegerField()
  away_score = IntegerField()
  gamekey = IntegerField()
  year = IntegerField()
  week = IntegerField()

  def winner(self):
    if self.home_score > self.away_score:
      return self.home_team
    return self.away_team

  def previous_games(self):
    in_previous_year = Game.year < self.year
    in_previous_week = Game.year == self.year & Game.week < self.week
    return Game.select().where(in_previous_year | in_previous_week)

  class Meta:
    database = db