### Hero Class ###
import random

class Hero():
    def __init__(self, name, character, number, health, damage, block, gold, blood, diamond):
        self.name = name
        self.charactertype = character
        self.number = number
        self.health = health
        self.damage = damage
        self.block = block
        self.gold = gold
        self.blood = blood
        self.diamond = diamond
        self.inventory = [1, 1, 1, 1]
        self.used = 0 


def generate_heros():
    hero_goblin = Hero("alex", "The sneaky goblin", 1, 100, 5, 3, 0, 0, 0)
    hero_archer = Hero("sam" , "The light Archer", 2, 200, 10, 7, 0, 0, 0)
    hero_knight = Hero("kevin", "The Shiny knight", 3, 400, 100, 13,0, 0, 0)
    hero_god = Hero("God", "The lord himself", 4, 4, 9999, 1, 9999, 9999, 9999)
    return(hero_goblin, hero_archer, hero_knight, hero_god)
