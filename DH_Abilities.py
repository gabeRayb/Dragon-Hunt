#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

############################# PLAYER ABILITY SETUP #############################
import DH_Character_Creation as CC

class ability:
    def __init__(self, name, description,r_cost):
        self.name = name
        self.description = description
        self.r_cost = r_cost
        
class offensive(ability):
    def __init__(self, name, description, r_cost, dmg):
        super().__init__(name, description, r_cost)
        self.dmg = dmg
    def use():
        pass
class defensive(ability):
     def __init__(self, name, description, r_cost, stat, buff):
        super().__init__(name, description, r_cost)
        self.stat = stat
        self.buff = buff
        
class utility(ability):
    def __init__(self, name, description, r_cost, effect):
        super().__init__(name, description, r_cost)
        self.effect = effect
#Mage starter ability   
fireball = offensive("Fireball","Hurls a firey orb at the enemy.", 10, 25)
heal = utility("Heal","Restores lost health points of caster.","health", 5,)

#Skeleton Abilities
slash = offensive("Slash","Swings bladed weapon/claws at the enemy.",0, 10)
fire_stream = offensive("Fire Stream","Blows a stream of fire at the enemy.",8,15)
bow_shot = offensive("Bow Shot","Fires an arrow at the enemy.",0, 10)