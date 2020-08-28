"""
Created on Wed Aug  5 16:53:13 2020
Authors: Johnnie Clark, Gabriel Rayburn
This file houses the tools for creating abilities as well as the abilities
themselves.
"""
#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

############################# PLAYER ABILITY SETUP #############################

class ability:
    """Ability hierarchy base class"""
    def __init__(self, name, description, r_cost):
        self.name = name
        self.description = description
        self.r_cost = r_cost
    def display(self):
        print("Name:", self.name)
        print("Description:", self.description)
        print("Mana cost:", self.r_cost)
class offensive(ability):
    """Offensive ability branch class"""
    def __init__(self, name, description, r_cost, dmg):
        super().__init__(name, description, r_cost)
        self.dmg = dmg
        # self.effect = effect
    def display(self):
        super().display()
        print("Dmg:", self.dmg)
        # print("Effect:", self.effect)
    def battle_display(self):
        print("Name:", self.name)
        print("Damage:", self.dmg)
        print("Mana cost:", self.r_cost)
class defensive(ability):
    """Defensive ability branch class"""
    def __init__(self, name, description, r_cost, stat, val):
        super().__init__(name, description, r_cost)
        self.stat = stat
        self.val = val
# class utility(ability):
#     def __init__(self, name, description, r_cost, price, effect):
#         super().__init__(name, description, r_cost, price)
#         self.effect = effect

# Mage abilities
fireball = offensive("Fireball", "Hurls a firey orb at the enemy.", 5, 20)
heal = defensive("Heal","Restores lost health points of caster.", 5, "health", 30,)

#Skeleton Abilities
# slash = offensive("Slash","Swings bladed weapon/claws at the enemy.",0, 10, "Bleed")
# fire_stream = offensive("Fire Stream","Blows a stream of fire at the enemy.",8,15)
# bow_shot = offensive("Bow Shot","Fires an arrow at the enemy.",0, 10)
