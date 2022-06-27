### Deployment Card Class ###
import random

class Action_Card():
    def __init__(self, name, cost, rarity, damage, move, block):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.damage = damage
        self.movement = move
        self.block = block