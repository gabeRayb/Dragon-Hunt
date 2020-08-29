"""
Created on Wed Aug 19 20:59:45 2020

@author: Gabriel Rayburn
"""
import DH_Character_Creation as CC
import numpy as np
import copy as copy

events_num = 2



#Lists of enemies for each chapter
enemies = {"ch1":[CC.wolf(), CC.skeleton(), CC.spider(), CC.bear()],
           "ch2":[CC.wisp(), CC.possessed_knight(), CC.elf_bandit(), CC.orc_bandit(), CC.goblin()],
           "ch3":[CC.animated_armor(), CC.shield_guardian(), CC.guard(), CC.shady_figure(), CC.soulless_aristocrat()],
           "ch4":[CC.troll(), CC.mountain_warrior(), CC.hermit(), CC.sorcerer()],
           "ch5":[CC.kobold(), CC.banshee(), CC.crab(), CC.shapeshifter(), CC.lake_dweller(), CC.water_devil()]}

#Mini bosses for each chapter
mini_bosses = {"ch1":CC.mother_of_wolves(),
               "ch2":CC.warchief(),
               "ch3":CC.centurion(),
               "ch4":CC.giant(),
               "ch5":CC.cultist_leader()}

#Boss for each chapter
bosses = {1:CC.revenant(),
          2:CC.war_machine(),
          3:CC.greed_demon(),
          4:CC.monstrosity(),
          5:CC.hydra()}
class event:
    def __init__(self, name, chapter):
        self.name = name
        self.chapter = chapter
class enemy_encounter(event):
    def __init__(self, name,chapter,enemy=None):
        super().__init__(name, chapter)
        # self.chapter = chapter
        self.enemy = copy.deepcopy(np.random.choice(enemies[f"ch{chapter}"])) #randomly choose an enemy from the appropriate chapter
    def display(self):
        print(f"You encountered a {self.enemy.name}!")
        # self.enemy.print_stats()
class mini_boss(event):
    def __init__(self,name,chapter,enemy = None):
        super().__init__(name, chapter)
        self.enemy = mini_bosses[f"ch{chapter}"]
    def display(self):
        print(f"You encountered an {self.enemy.name}, the chapter mini boss!")
class boss(event):
    def __init__(self, name, chapter, enemy = None):
        super().__init__(name, chapter)
        self.enemy = bosses[chapter]
    def display(self):
        print(f"You encountered an {self.enemy.name}, the chapter boss!")
def roll_event(chapter):
    return copy.deepcopy(np.random.choice(events[f"ch{chapter}"]))

events = {"ch1":[],
          "ch2":[],
          "ch3":[],
          "ch4":[],
          "ch5":[]}
boss_events = {"ch1":None,
               "ch2":None,
               "ch3":None,
               "ch4":None,
               "ch5":None}
for i in range(1,6):
    events[f"ch{i}"].append(mini_boss("Mini-boss Encounter",i))
    boss_events[f"ch{i}"] = boss("Boss Encounter", i)
    for j in range(8):
        events[f"ch{i}"].append(enemy_encounter("Enemy Encounter",i))