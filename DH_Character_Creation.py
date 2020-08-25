# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:53:13 2020

Authors: Johnnie Clark, Gabriel Rayburn
"""
import numpy as np

############################ ENEMY CHARACTER SETUP ############################

######## Basic Enemies ########

class basic_enemy:
    def __init__(self, level = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        self.level = 1
        self.effects = []
        self.abilities = []
        self.death_exp = 20
        self.base_gold_drop = 100
        self.gold_drop_mult = 1.1

    def display_abilities(self):
        for i in self.abilities:
            print(i)
            
    def info(self):
        print('Level:', self.level)
            
#### Village 1 Enemies ####

class wolf(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Wolf'
        self.health = 70 * level
        self.attack = np.random.randint(15,21) * level
        self.defense = np.random.randint(20,26) * level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class skeleton(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Skeleton'
        self.items = []
        self.health = 100 * level
        self.attack = 0
        self.defense = 0

    def display_items(self):
        for i in self.items:
            print(i)

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class spider(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Poisonous Spider'
        self.health = 50 * level
        self.attack = np.random.randint(5,11) * level
        self.defense = np.random.randint(10,16) * level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class bear(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Enraged Bear'
        self.health = 150 * level
        self.attack = np.random.randint(20,26) * level
        self.defense = np.random.randint(40,51) * level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 2 Enemies ####

class wisp(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Wisp'
        self.health = 120 * level
        self.attack = np.random.randint(10,16) * level
        self.defense = np.random.randint(15,21) * level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

def possessed_knight(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Possessed Knight'
        self.items = []
        self.health = 200 * level
        self.attack = 0
        self.defense = 0
            
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def elf_bandit(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Elf Bandit'
        self.items = []
        self.health = 140 * level
        self.attack = 0
        self.defense = 0
            
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def orc_bandit(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)        
        self.name = 'Orc Bandit'
        self.items = []
        self.health = 180 * level
        self.attack = 0
        self.defense = 0
            
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def goblin(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Goblin'
        self.items = []
        self.health = 110 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 3 Enemies ####

class animated_armor(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Animated Armor'
        self.health = 200 * level
        self.attack = np.random.randint(25,31) * level
        self.defense = np.random.randint(40,51) * level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class shield_guardian(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Shield Guardian'
        self.health = 250 * level
        self.attack = np.random.randint(20,36) * level
        self.defense = np.random.randint(45,56) * level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class guard(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Corrupt Guard'
        self.items = []
        self.health = 150 * level
        self.attack = 0
        self.defense = 0

    def display_items(self):
        for i in self.items:
            print(i)

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

def shady_figure(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Shady Figure'
        self.items = []
        self.health = 125 * level
        self.attack = 0
        self.defense = 0

    def display_items(self):
        for i in self.items:
            print(i)

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

def soulless_aristocrat(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Soulless Aristocrat'
        self.items = []
        self.health = 135 * level
        self.attack = 0
        self.defense = 0

    def display_items(self):
        for i in self.items:
            print(i)

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 4 Enemies ####

def troll(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Frost Troll'
        self.health = 265 * level
        self.attack = np.random.randint(30, 36) * level
        self.defense = np.random.randint(35, 46) * level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

def mountain_warrior(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Mountain Warrior'
        self.items = []
        self.health = 245 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def hermit(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Deranged Hermit'
        self.items = []
        self.health = 230 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def sorcerer(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Dark Sorcerer'
        self.items = []
        self.health = 210 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
#### Village 5 Enemies ####

def kobold(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Kobold'
        self.items = []
        self.health = 270 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def banshee(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Banshee'
        self.health = 265 * level
        self.attack = np.random.randint(30, 36) * level
        self.defense = np.random.randint(35, 51) * level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def crab(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Giant Crab'
        self.health = 325 * level
        self.attack = np.random.randint(25, 36) * level
        self.defense = np.random.randint(50, 66) * level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def shapeshifter(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Shapeshifter'
        self.health = np.random.randint(210, 301) * level
        self.attack = np.random.randint(25, 46) * level
        self.defense = np.random.randint(40, 56) * level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def lake_dweller(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Lake Dweller'
        self.items = []
        self.health = 235 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
def water_devil(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Water Devil'
        self.health = 210 * level
        self.attack = np.random.randint(40, 46) * level #(1.0 + level/10)
        self.defense = np.random.randint(30,41) * level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

######## Mini Bosses ########

class mini_boss():
    def __init__(self, level = None, effects = None, abilites = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        self.level = 1
        self.effects = []
        self.abilities = []
        self.death_exp = 50
        self.base_gold_drop = 100
        self.gold_drop_mult = 1.1

    def calc_gold_drop(self):
        return (self.base_gold_drop*(self.gold_drop_mult+1.5)) + self.level
    
    def display_abilities(self):
        for i in self.abilities:
            print(i)

    def info(self):
        print('Level:', self.level)

#### Village 1 Mini Boss ####

class mother_of_wolves(mini_boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Mother of Wolves'
        self.health = 250 * level
        self.attack = np.random.randint(30,36) * level
        self.defense = np.random.randint(55,61) * level
            
    def print_stats(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 2 Mini Boss ####

class warchief(mini_boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Bandit Warchief'
        self.items = []
        self.health = 450 * level
        self.attack = 0
        self.defense = 0
            
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 3 Mini Boss ####

class centurion(mini_boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Dwarven Centurion'
        self.items = []
        self.health = 450 * level
        self.attack = 0
        self.defense = 0
            
    def display_items(self):
        for i in self.items:
            print(i)
        
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 4 Mini Boss ####

class giant(mini_boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Royal Giant'
        self.items = []
        self.health = 450 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
#### Village 5 Mini Boss ####

class hydra(mini_boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Hydra'
        self.health = 450 * level
        self.attack = np.random.randint(40, 51) * level
        self.defense = np.random.randint(65, 81) * level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
######## Bosses ########

def boss():
    def __init__(self, level = None, effects = None, abilites = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        self.level = 1
        self.effects = []
        self.abilities = []
        self.death_exp = 100
        self.base_gold_drop = 100
        self.gold_drop_mult = 1.1
    
    def calc_gold_drop(self):
        return (self.base_gold_drop*(self.gold_drop_mult+2.0)) + self.level
    
    def display_abilities(self):
        for i in self.abilities:
            print(i)

    def info(self):
        print('Level:', self.level)
        
#### Village 1 Boss ####

def revanent(boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Revanent'
        self.items = []
        self.health = 550 * level
        self.attack = 0
        self.defense = 0
        
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
#### Village 2 Boss ####

def war_machine(boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'War Machine'
        self.health = 550 * level
        self.attack = np.random.randint(40, 61) * level
        self.defense = np.random.randint(60, 71) * level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 3 Boss ####



#### Village 4 Boss ####



#### Village 5 Boss ####

#### Final Boss ####

def world_breaker(boss):
    pass        

###############################################################################

############################ PLAYER CHARACTER SETUP ############################

class player_setUp: # Base class for setting up a character
    def __init__(self, name, race, effects = None, currExp = None, neededExp = None, level = None, action = None, abilities = None, items = None, gold = None):
        self.name = name
        self.race = race
        self.abilities = []
        self.effects = []
        self.items = []
        self.gold = 0
        self.currExp = 0
        self.neededExp = 100
        self.level = 1
        
    def display_abilities(self):
        for i in self.abilities:
            print(i)
            
    def display_items(self):
        for i in self.items:
            print(i)
            
    def info(self):
        print('Name:', self.name)
        print('Race:', self.race)
        print('Gold:', self.gold)
        print('Experience: {}/{}'.format(self.currExp, self.neededExp))
        print('Level:', self.level)
        
    def levelUp(self):
        self.level += 1
        self.health += 5
        self.mana += 5
        
class mage(player_setUp): 
    def __init__(self, name, race, player_class, health = None, mana = None, dmg_mult = None, attack = None, defense = None, effects = None, currExp = None, neededExp = None, level = None, action = None, abilities = None, items = None, gold = None):
        super().__init__(name, race, abilities, effects, items, gold, currExp, neededExp, level)
        self.player_class = player_class
        self.health = 100
        self.mana = 120
        self.dmg_mult = 1.0
        self.attack = 0
        self.defense = 0
        
    def info(self):
        super().info()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
    
class warrior(player_setUp):
    def __init__(self, name, race, player_class, health = None, mana = None, dmg_mult = None, attack = None, defense = None, effects = None, currExp = None, neededExp = None, level = None, action = None, abilities = None, items = None, gold = None):
        super().__init__(name, race, abilities, effects, items, gold, currExp, neededExp, level)
        self.player_class = player_class
        self.health = 120
        self.mana = 80
        self.dmg_mult = 1.0
        self.attack = 0
        self.defense = 0
        
    def info(self):
        super().info()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
    
class rogue(player_setUp):
    def __init__(self, name, race, player_class, health = None, mana = None, dmg_mult = None, attack = None, defense = None, effects = None, currExp = None, neededExp = None, level = None, action = None, abilities = None, items = None, gold = None):
        super().__init__(name, race, abilities, effects, items, gold, currExp, neededExp, level)
        self.player_class = player_class
        self.health = 80
        self.mana = 100
        self.dmg_mult = 1.1
        self.attack = 0
        self.defense = 0

    def info(self):
        super().info()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
        
################################################################################