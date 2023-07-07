import random

class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.roll = None


    def player_roll(self, options):
        self.roll = random.choice(options)


