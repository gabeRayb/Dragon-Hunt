# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:53:13 2020

Authors: Johnnie Clark, Gabriel Rayburn
"""
import numpy as np

############################ ENEMY CHARACTER SETUP ############################

class basic_enemy:
    def __init__(self, death_exp = None):
        self.death_exp = 20

class wolf(basic_enemy):
    def __init__(self, name = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None):
        self.name = 'Wolf'
        self.effects = []
        self.abilities = []
        self.health = 70
        self.attack = np.random.randint(10,21)
        self.defense = np.random.randint(20,26)

    def print_stats(self):
        print('Enemy:', self.name)
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class skeleton(basic_enemy):
    def __init__(self, name = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None, items = None):
        self.name = 'Skeleton'
        self.effects = []
        self.abilities = []
        self.items = []
        self.health = 100
        self.attack = 0
        self.defense = 0

    def display_abilities(self):
        for i in self.abilities:
            print(i)
            
    def print_stats(self):
        print('Enemy:', self.name)
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class spider(basic_enemy):
    def __init__(self, name = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None):
        self.name = 'Poisonous Spider'
        self.effects = []
        self.abilities = []
        self.health = 50
        self.attack = np.random.randint(5,11)
        self.defense = np.random.randint(10,16)

    def print_stats(self):
            print('Enemy:', self.name)
            print('Health:', self.health)
            print('Attack:', self.attack)
            print('Defense:', self.defense)
        
class bear(basic_enemy):
    def __init__(self, name = None, health = None, attack = None, defense = None, effects = None, action = None, abilities = None):
        self.name = 'Enraged Bear'
        self.effects = []
        self.abilities = []
        self.health = 150
        self.attack = np.random.randint(25,31)
        self.defense = np.random.randint(40,51)
        
    def print_stats(self):
        print('Enemy:', self.name)
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
###############################################################################

############################ PLAYER CHARACTER SETUP ############################

class player_setUp: # Base class for setting up a character
    def __init__(self, name, race, effects = None, currExp = None, neededExp = None, level = None, action = None, abilities = None, items = None):
        self.name = name
        self.race = race
        self.abilities = []
        self.effects = []
        self.items = []
        self.currExp = 0
        self.neededExp = 100
        self.level = 1
        
    def display_abilities(self):
        for i in self.abilities:
            print(i)
            
    def display_items(self):
        for i in self.items:
            print(i)
            
    def print_stats(self):
        print('Name:', self.name)
        print('Race:', self.race)
        print('Experience: {}/{}'.format(self.currExp, self.neededExp))
        print('Level:', self.level)
        
    def levelUp(self):
        self.level += 1
        self.health += 5
        self.mana += 5
        
class mage(player_setUp): 
    def __init__(self, name, race, player_class, health = None, mana = None, dmg_mult = None, attack = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 100
        self.mana = 120
        self.dmg_mult = 1.0
        self.attack = 0
        self.defense = 0
        
    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
    
class warrior(player_setUp):
    def __init__(self, name, race, player_class, health = None, rage = None, max_rage = None, dmg_mult = None, attack = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 200
        self.rage = 0
        self.max_rage = 100
        self.dmg_mult = 1.0
        self.attack = 0
        self.defense = 0
        
    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Max Rage:', self.max_rage)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
    
class rogue(player_setUp):
    def __init__(self, name, race, player_class, health = None, mana = None, dmg_mult = None, attack = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 150
        self.mana = 150
        self.dmg_mult = 1.1
        self.attack = 0
        self.defense = 0

    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
        
################################################################################

############################# PLAYER ABILITY SETUP #############################

class ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
class offensive(ability):
    def __init__(self, name, description, dmg):
        super().__init__(name, description)
        self.dmg = dmg
        
class defensive(ability):
     def __init__(self, name, description, buff):
        super().__init__(name, description)
        self.buff = buff
        
class utility(ability):
    def __init__(self, name, description, effect):
        super().__init__(name, description)
        self.effect = effect
    
################################################################################
 
offensive_abilities = []
defensive_abilities = []
utility_abilities = []