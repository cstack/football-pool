from strategy import strategies
from orm import *

games = Game.select()
total = games.count()
for strategy in strategies:
  correct = 0
  for game in games:
    if strategy().predict(game) == game.winner():
      correct += 1
  print "strategy {0}".format(strategy.__name__)
  print "{0} / {1} : {2} %".format(correct, total, round(float(correct) / total * 100, 2))
