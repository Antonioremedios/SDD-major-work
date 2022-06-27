### Enemy Class ###
import random

from numpy import block

class EnemyNPC():
    def __init__(self, name, health, damage, block):
        self.name = name
        self.damage = damage
        self.health = health
        self.block = block

# Subclass of EnemyNPC called boss

class EnemyBoss(EnemyNPC):
    def __init__(self, name, health, damage, block, aspect):
        super().__init__(name, health, damage, block)
        self.aspect = aspect


def instantiate_enemies(names, max_hp, min_hp, max_dam, min_dam, max_block, min_block):
    enemies = []
    for i in range(0,300):
        enemy = EnemyNPC(names[random.randint(0, len(names)-1)], 
                                random.randint(min_hp, max_hp), 
                                random.randint(min_dam, max_dam), 
                                random.randint(min_block, max_block))
        enemies.append(enemy)
    return enemies

def generate_enemies():
    # map_1
    meadow_enemy_types = ["Mutant Rat", "Rock Thrower", "Ticklish Thief", "Peasent", "Hutman"]
    max_hp = 100
    min_hp = 50
    max_dam = 17
    min_dam = 8
    max_block = 11
    min_block = 6
    map_1_enemies = instantiate_enemies(meadow_enemy_types, 
                                        max_hp , min_hp, 
                                        max_dam, min_dam, 
                                        max_block, min_block)
    map_1_boss = EnemyBoss("Obnoxious Orgre", 100, 10, 10, "Grass")

    # map_2 
    valley_enemy_types = ["Longbowman", "Crossbowman", "Ambusher", "Stalker"]
    max_hp = 150
    min_hp = 75
    max_dam = 29
    min_dam = 15
    max_block = 18
    min_block = 11
    map_2_enemies = instantiate_enemies(valley_enemy_types, 
                                        max_hp , min_hp, 
                                        max_dam, min_dam, 
                                        max_block, min_block)
    map_2_boss = EnemyBoss("Stone Giant", 200, 20, 15, "Wind")

    # map_3
    forrest_enemy_types = ["Caster", "Tree man", "Shape Shifter"]
    max_hp = 200    
    min_hp = 100
    max_dam = 35
    min_dam = 19
    max_block = 23
    min_block = 16
    map_3_enemies = instantiate_enemies(forrest_enemy_types, 
                                        max_hp , min_hp, 
                                        max_dam, min_dam, 
                                        max_block, min_block)
    map_3_boss = EnemyBoss("Dark Archer", 400, 30, 25, "Rain")

    # map_4
    ancients_enemy_types = ["Mummy" , "Anubis", "Camel Soilder"]
    max_hp = 250
    min_hp = 125
    max_dam = 40
    min_dam = 24
    max_block = 28
    min_block = 20
    map_4_enemies = instantiate_enemies(ancients_enemy_types, 
                                        max_hp , min_hp, 
                                        max_dam, min_dam, 
                                        max_block, min_block)
    map_4_boss = EnemyBoss("Corrupted Pharaoh", 600, 40, 35, "Sand")

    # map_5
    volcano_enemy_types = ["Fire Spirit" , "Fire caster", "Hardened Man", "Disovled Crab"]
    max_hp = 300
    min_hp = 200
    max_dam = 45
    min_dam = 29
    max_block = 34
    min_block = 25
    map_5_enemies = instantiate_enemies(volcano_enemy_types, 
                                        max_hp , min_hp, 
                                        max_dam, min_dam, 
                                        max_block, min_block)
    map_5_boss = EnemyBoss("Scorched Dragon", 1000, 80, 50, "Fire")

    return (map_1_enemies, map_1_boss
        , map_2_enemies, map_2_boss
        , map_3_enemies, map_3_boss
        , map_4_enemies, map_4_boss
        , map_5_enemies, map_5_boss)