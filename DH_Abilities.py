#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

############################# PLAYER ABILITY SETUP #############################

class ability:
    def __init__(self, name, description,r_cost, price):
        self.name = name
        self.description = description
        self.r_cost = r_cost
    
    def display(self):
        print("Name:", self.name)
        print("Description:", self.description)
        print("Mana cost:", self.r_cost)
        
class offensive(ability):
    def __init__(self, name, description, r_cost, price, dmg, effect):
        super().__init__(name, description, r_cost, price)
        self.dmg = dmg
        self.effect = "None"
    def display(self):
        super().display()
        print("Dmg:", self.dmg)
        print("Effect:", self.effect)
        
class defensive(ability):
     def __init__(self, name, description, r_cost, price, stat, buff):
        super().__init__(name, description, r_cost, price)
        self.stat = stat
        self.buff = buff
        
# class utility(ability):
#     def __init__(self, name, description, r_cost, price, effect):
#         super().__init__(name, description, r_cost, price)
#         self.effect = effect
#Mage starter ability   
fireball = offensive("Fireball","Hurls a firey orb at the enemy.", 10, 20, 25, "Burn")
# heal = utility("Heal","Restores lost health points of caster.","health", 5,)

#Skeleton Abilities
# slash = offensive("Slash","Swings bladed weapon/claws at the enemy.",0, 10, "Bleed")
# fire_stream = offensive("Fire Stream","Blows a stream of fire at the enemy.",8,15)
# bow_shot = offensive("Bow Shot","Fires an arrow at the enemy.",0, 10)