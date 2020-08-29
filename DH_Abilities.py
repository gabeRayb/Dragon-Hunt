"""
Created on Wed Aug  5 16:53:13 2020
Authors: Johnnie Clark, Gabriel Rayburn
This file houses the tools for creating abilities as well as the abilities
themselves.
"""
#Author: Gabriel Rayburn, Johnnie Clark
#Created 7/9/2020
#Open Source Project: Dragon Hunt

from collections import deque

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

############################## PLAYER ABILITIES ##############################

######## Neutral class abilities ########

####starting abilities####
heal = defensive("Heal","Restores lost health points of caster.", 5, "Health", 30) # lvl 1
barrier = defensive('Barrier', 'Temporarily increase the users defense.', 10, 'Defense', 5) # lvl 1
##########################

revitalize = defensive('Revitalize', 'Increase your max health.', 20, 'Health', 50) # lvl 4

######## Mage abilities ########
mage_locked_abilities = deque() # [meteor_shower, winter_beam, acid_spores, hail, impale, revitalize, daing_bolt, short_circuit]

# starting ability
fireball = offensive("Fireball", "Hurls a firey orb at the enemy.", 5, 20) # lvl 1

#expert
meteor_shower = offensive('Meteor Shower', 'Large balls of fire rain down from the sky over the enemy.', 95, 300) # lvl 12

#intermediate
winter_beam = offensive('Winter Beam', 'Shoot an ice cold beam at the enemy.', 32, 130) # lvl 9
acid_spores = offensive('Acid Spores', 'Shoot spores of acid at the enemy.', 30, 125) # lvl 8
hail = offensive('Hail', 'Ice spikes rain down from the sky over the enemy', 20, 62) # lvl 6

#improved
impale = offensive('Impale', 'Summon a spike made from the earth to impale the enemy.', 12, 45) # lvl 5
dazing_bolt = offensive('Dazing Bolt', 'Summon a bolt of lightning from the sky to strike the enemy', 10, 40) # lvl 3

#basic
short_circuit = offensive('Short Circuit', 'Excite the air partlicles around the enemy creating a static field and electricuting them.', 8, 30) # lvl 2

# Store mage abilities
mage_locked_abilities.append(meteor_shower)
mage_locked_abilities.append(winter_beam)
mage_locked_abilities.append(acid_spores)
mage_locked_abilities.append(hail)
mage_locked_abilities.append(impale)
mage_locked_abilities.append(revitalize)
mage_locked_abilities.append(dazing_bolt)
mage_locked_abilities.append(short_circuit)


# Warrior abilities
warrior_locked_abilities = deque()

#Starting Ability
puncture = offensive('Puncture', 'Take a wild stab at the enemy.', 10, 25) # lvl 1

#basic
sucker_punch = offensive('Sucker Punch', 'Hit the enemy when he least expects it.', 5, 15) # lvl 2
whirlwind = offensive('Whirlwind', 'Spin really fast to hit stuff.', 15, 40) # lvl 3

#improved
enrage = defensive('Enrage', "You're filled with anger. You know put everything you have into every attack.", 40, 'Attack', 25) # lvl 5

#intermediate
blitz = offensive('Blitz', 'Dash at incredible speed to strike the enemy.', 25, 65) # lvl 6
overpower = offensive('Overpower', 'With all your might, leap into the air and slam the enemy with your weapon.', 30, 120) # lvl 8

#expert
execute = offensive('Execute', 'Deal massive damage to the enemy.', 40, 210) # lvl 9
onslaught = offensive('Onslaught', 'Overwhelm the enemy with a flurry of attacks.', 55, 315) # lvl 12

#Store warrior abilities
warrior_locked_abilities.append(onslaught)
warrior_locked_abilities.append(execute)
warrior_locked_abilities.append(overpower)
warrior_locked_abilities.append(blitz)
warrior_locked_abilities.append(enrage)
warrior_locked_abilities.append(revitalize)
warrior_locked_abilities.append(whirlwind)
warrior_locked_abilities.append(sucker_punch)

# Rogue abilities
rogue_locked_abilities = deque()

#Starting ability
pierce = offensive('Pierce', 'Take a stab at the enemy.', 8, 22) # lvl 1

#basic
back_stab = offensive('Back Stab', 'Stab the enemy in the back.', 10, 28) # lvl 2
throw_knife = offensive('Throw Knife', 'Throw a knife at the enemy.', 12, 32) # lvl 3

#imporved
rupture = offensive('Rupture', 'Slash at the enemies tendons.', 20, 50) # lvl 5
cloak_dagger = offensive('Cloak and Dagger', 'Disappear and reaper after stabing the enemy.', 32, 75) # lvl 6
sacrifice = defensive('Sacrifice', 'Increase damage', 35, 'Attack', 30) # lvl 8 give some health to increase dmg

#expert
terrifying_cruelty = offensive('Terrifying Cruelty', 'Repeatedly stab the enemy causing massive damage.', 50, 215) # lvl 9
mortal_blow = offensive('Mortal Blow', 'Stab at the enemies major organs.', 65, 400) # lvl 12

#Store rogue abilities
rogue_locked_abilities.append(mortal_blow)
rogue_locked_abilities.append(terrifying_cruelty)
rogue_locked_abilities.append(sacrifice)
rogue_locked_abilities.append(cloak_dagger)
rogue_locked_abilities.append(rupture)
rogue_locked_abilities.append(revitalize)
rogue_locked_abilities.append(throw_knife)
rogue_locked_abilities.append(back_stab)

# ############################ BASIC ENEMY ABILITIES ############################

# ######## Village 1 ########

# Wolf Abilities
# wolf_abilities = []
# wolf_abilities.append(bite = offensive('Bite', 'Bite into the enemy.', 0, 12))
# wolf_abilities.append(scratch = offensive('Scratch', 'Scratch the enemy with claws.', 0, 15))
# wolf_abilities.append(howl = defensive('Howl', 'Increase damage.', 0, 'Attack', 5))

# # Skeleton Abilities & Goblin (Village 2)
# skel_abilities = []
# skel_abilities.append(slash = offensive("Slash","Swings bladed weapon/claws at the enemy.", 0, 10))
# skel_abilities.append(thrust = offensive('Thrust', 'Thrust your weapon at the enemy.', 0, 15))

# # Spider Abilities
# spider_abilities = []
# spider_abilities.append(inject = offensive('Inject', 'Bite into the enemy, injecting venom.', 0, 10))
# spider_abilities.append(venemous_spray = offensive('Venemous Spray', 'Spray venom at the enemy.', 0, 12))

# # Bear Abilities
# bear_abilities = []
# bear_abilities.append(claw = offensive('Claw', 'Swipe at the enemy with massive claws.', 0, 10))
# bear_abilities.append(charge = offensive('Charge', 'Rush to attack the enemy at full speed.', 0, 15))
# bear_abilities.append(thick_coat = defensive('Thick Coat', 'Increase defense.', 0, 'Defense', 5))
# bear_abilities.append(forest_predator = defensive('Forest Predator', 'Increase Attack', 0, 'Attack', 5))

# # Mini Boss Abilities
# m_o_w_abilities = []
# m_o_w_abilities.append(devour = offensive('Devour', 'Clasp the enemy with massive jaws and ragdoll the enemy.', 0, 20))
# m_o_w_abilities.append(gut = offensive('Gut', 'Slash the enemy with massive claws.', 0, 25))

# # Boss Abilities
# revenant_abilities = []
# revenant_abilities.append(void_slash = offensive('Void Slash', 'Slash the enemy with the power of the void.', 0, 25))
# revenant_abilities.append(gag_order = offensive('Gag Order', 'Choke the life out of the enemy through power of the void.', 0, 30))

# ######## Village 2 ########

# # Wisp Abilities
# ice_spike = offensive('Ice Spike', 'Shoots an ice spike at the enemy.', )
# knaw = offensive('Knaw', 'Bite the enemy.', )

# # Possessed Knight Abilities
# cleave = offensive('Cleave', 'Swing your weapon with enough force to cut your enemy in half.', )
# shield_up = defensive('Shield Up', 'Increase defense.', )
# helm_splitter = offensive('Helm Splitter', 'Slash down on the enemy with incredible power.', )
# void_conduit = defensive('Void Conduit', 'Increase attack', 'Attack', )

# # Elf Bandit
# explosive_shot = offensive("Explosive Shot","Fires an explosive arrow at the enemy.", 0, 10)
# sharpen_arrows = defensive('Sharpen Arrows', 'Increase attack.', 'Attack', )
# ballistic_shot = offensive('Ballistic Shot', 'Fires an arrow at high velocity at the enemy.', )

# # Orc Bandit
# axe_throw = offensive('Axe Throw', 'Throw an axe at the enemy.', )
# hack_slash = offensive('Hack and Slash', 'Swing wildly at the enemy with your weapon(s).', )
# encourage = defensive('Encourage', 'Increase attack.', 'Attack', )
# fight_dirty = offensive('Fight Dirty', 'Throw dirt in the enemies face in order to close the distance and land a solid blow.', )

# # Goblin (see Skeleton abilities)

# ######## Village 3 ########

# # Animated Armor Abilities

#Skeleton Abilities
# slash = offensive("Slash","Swings bladed weapon/claws at the enemy.",0, 10, "Bleed")
# fire_stream = offensive("Fire Stream","Blows a stream of fire at the enemy.",8,15)
# bow_shot = offensive("Bow Shot","Fires an arrow at the enemy.",0, 10)
