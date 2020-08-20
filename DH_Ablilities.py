#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

############################# PLAYER ABILITY SETUP #############################

class ability:
    def __init__(self, name, description,r_cost):
        self.name = name
        self.description = description
        self.r_cost = r_cost
        
class offensive(ability):
    def __init__(self, name, description, r_cost, dmg):
        super().__init__(name, description, r_cost)
        self.dmg = dmg
        
class defensive(ability):
     def __init__(self, name, description, r_cost, buff):
        super().__init__(name, description, r_cost)
        self.buff = buff
        
class utility(ability):
    def __init__(self, name, description, r_cost, effect):
        super().__init__(name, description, r_cost)
        self.effect = effect
    
fireball = offensive("Fireball","Hurls a firey orb at the opponent.", 10, 25)
    
    