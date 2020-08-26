"""
Created on Wed Aug 19 20:59:45 2020

@author: Gabriel Rayburn
"""
import DH_Character_Creation as CC
import numpy as np

events_num = 2



#Lists of enemies for each chapter
enemies = {"ch1":[CC.wolf(),CC.skeleton(),CC.spider()],
           "ch2":[CC.wolf(),CC.skeleton(),CC.spider()],
           "ch3":[CC.wolf(),CC.skeleton(),CC.spider()],
           "ch4":[CC.wolf(),CC.skeleton(),CC.spider()],
           "ch5":[CC.wolf(),CC.skeleton(),CC.spider()]}

#Mini bosses for each chapter
mini_bosses = {"ch1":CC.bear(),
               "ch2":CC.bear(),
               "ch3":CC.bear(),
               "ch4":CC.bear(),
               "ch5":CC.bear()}

class event:
    def __init__(self, name):
        self.name = name

class enemy_encounter(event):
    def __init__(self, name,chapter,enemy=None):
        super().__init__(name)
        self.chapter = chapter
        self.enemy = np.random.choice(enemies[f"ch{chapter}"]) #randomly choose an enemy from the appropriate chapter

    def display(self):
        print(f"You encountered a {self.enemy.name}!")
        # self.enemy.print_stats()

class mini_boss(event):
    def __init__(self,name,chapter,m_b=None):
        super().__init__(name)
        self.chapter = chapter
        self.enemy = mini_bosses[f"ch{chapter}"]
    
    def display(self):
        print(f"You encountered an {self.enemy.name}, the chapter mini boss!")
        # self.m_b.print_stats()

events = [enemy_encounter("Enemy Encounter",1)]*5 + [mini_boss("Mini-boss Encounter",1)]*5

def roll_event():
    return np.random.choice(events)
    

