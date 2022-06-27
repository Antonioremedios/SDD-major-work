### Deployment Card Class ###
import random

class Action_Scroll():
    def __init__(self, name, damage, block):
        self.name = name
        self.damage = damage
        self.block = block

def generate_scrolls():
    grass_scroll = Action_Scroll("Grass Scroll", 10, 8)
    fire_scroll = Action_Scroll("Fire Scroll", 50, 0)
    ice_scroll = Action_Scroll("Ice Scroll", 20, 60)
    plasma_scroll = Action_Scroll("Plasma Scroll", 50, 50)
    return(grass_scroll, fire_scroll, ice_scroll, plasma_scroll)
