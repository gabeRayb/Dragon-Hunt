"""
Created on Wed Aug 19 20:59:45 2020

@author: Gabriel Rayburn
"""
import DH_Character_Creation as CC
import numpy as np

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

class event:
    def __init__(self, name, chapter):
        self.name = name
        self.chapter = chapter
class enemy_encounter(event):
    def __init__(self, name,chapter,enemy=None):
        super().__init__(name, chapter)
        # self.chapter = chapter
        self.enemy = np.random.choice(enemies[f"ch{chapter}"]) #randomly choose an enemy from the appropriate chapter
    def display(self):
        print(f"You encountered a {self.enemy.name}!")
        # self.enemy.print_stats()
class mini_boss(event):
    def __init__(self,name,chapter,m_b=None):
        super().__init__(name, chapter)
        # self.chapter = chapter
        self.enemy = mini_bosses[f"ch{chapter}"]
    def display(self):
        print(f"You encountered an {self.enemy.name}, the chapter mini boss!")
        # self.m_b.print_stats()
def roll_event(chapter):
    return np.random.choice(events[f"ch{chapter}"]).copy()

chapter_1 = [enemy_encounter("Enemy Encounter",1)]*9 + [mini_boss("Mini-boss Encounter",1)]*1
chapter_2 = [enemy_encounter("Enemy Encounter",2)]*9 + [mini_boss("Mini-boss Encounter",2)]*1
chapter_3 = [enemy_encounter("Enemy Encounter",3)]*9 + [mini_boss("Mini-boss Encounter",3)]*1
chapter_4 = [enemy_encounter("Enemy Encounter",4)]*9 + [mini_boss("Mini-boss Encounter",4)]*1
chapter_5 = [enemy_encounter("Enemy Encounter",5)]*9 + [mini_boss("Mini-boss Encounter",5)]*1
events = {"ch1":chapter_1,
          "ch2":chapter_2,
          "ch3":chapter_3,
          "ch4":chapter_4,
          "ch5":chapter_5}

    

