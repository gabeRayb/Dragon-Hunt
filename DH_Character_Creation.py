"""
Authors: Johnnie Clark, Gabriel Rayburn

Project Name: Dragon Hunt
"""

############################### BATTLE SYSTEM ###############################
def attack(attacker, defender):
    pass

def defend(defender, attacker):
    pass

#############################################################################

############################ ENEMY CHARACTER SETUP ############################

class enemy:
    def __init__(self, name):
        pass
    
class skeleton(enemy):
    def __init__(self, name, enemy_type):
        pass


###############################################################################

############################ PLAYER CHARACTER SETUP ############################

class player_setUp: # Base class for setting up a character
    def __init__(self, name, race, currExp = None, neededExp = None, level = None):
        self.name = name
        self.race = race
        self.currExp = 0
        self.neededExp = 100
        self.level = 1
        
    def print_stats(self):
        print('Name:', self.name)
        print('Race:', self.race)
        print('Experience: {}/{}'.format(self.currExp, self.neededExp))
        print('Level:', self.level)
        
    # def levelUp(self):
    #     self.level += 1
    #     self.neededExp += self.neededExp*3.5
    #     self.health += self.health*0.1
    #     self.mana += self.mana*0.1
    #     self.phy_att = self.phy_att*0.1
    #     self.mag_att = self.mag_att*0.1
    #     self.defense = self.defense*0.1
        
class mage(player_setUp): 
    def __init__(self, name, race, player_class, health = None, mana = None, phy_att = None, mag_att = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 100
        self.mana = 200
        self.phy_att = 5
        self.mag_att = 20
        self.defense = 10
        
    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Physical Attack:', self.phy_att)
        print('Magical Attack:', self.mag_att)
        print('Defense:', self.defense)
        print('\n')
    
class warrior(player_setUp):
    def __init__(self, name, race, player_class, health = None, rage = None, max_rage = None, phy_att = None, mag_att = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 200
        self.rage = 0
        self.max_rage = 100
        self.phy_att = 15
        self.mag_att = 10
        self.defense = 20
        
    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Max Rage:', self.max_rage)
        print('Physical Attack:', self.phy_att)
        print('Magical Attack:', self.mag_att)
        print('Defense:', self.defense)
        print('\n')
    
class rogue(player_setUp):
    def __init__(self, name, race, player_class, health = None, mana = None, phy_att = None, mag_att = None, defense = None):
        super().__init__(name, race)
        self.player_class = player_class
        self.health = 150
        self.mana = 150
        self.phy_att = 20
        self.mag_att = 5
        self.defense = 15

    def print_stats(self):
        super().print_stats()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Physical Attack:', self.phy_att)
        print('Magical Attack:', self.mag_att)
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
    
    
offensive_abilities = []
defensive_abilities = []
utility_abilities = []

name = input('Enter character name: ')
race = input('Enter the race of your character: ').capitalize()
pClass = input('What class would you like to play as? (Warrior, Mage, Rogue): ').capitalize()
print('\n')

if pClass == 'Warrior':
    p1 = warrior(name, race, pClass)
    
if pClass == 'Mage':
    p1 = mage(name, race, pClass)
    
if pClass == 'Rogue':
    p1 = rogue(name, race, pClass)
    
p1.print_stats()


