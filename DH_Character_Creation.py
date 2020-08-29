# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:53:13 2020
Authors: Johnnie Clark, Gabriel Rayburn
"""
import numpy as np
import DH_Items as item
import DH_Abilities as ability
#from collections import deque

############################ ENEMY CHARACTER SETUP ############################

######## Basic Enemies ########

class basic_enemy:
    def __init__(self, level = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        self.level = 1
        self.effects = []
        self.abilities = {}
        self.death_exp = 20
        self.base_gold_drop = 100
        self.gold_drop_mult = 1.0 + self.level/10

    def display_abilities(self):
        for i in self.abilities:
            self.abilities[i].display()
            print('\n')
            
    def battle_display(self):
        for i in self.abilities:
            self.abilities[i].battle_display()
            print('\n')
        
    def calc_gold_drop(self):
        return (self.base_gold_drop*(self.gold_drop_mult+1.5)) + self.level
    
    def info(self):
        print('Level:', self.level)
            
#### Village 1 Enemies ####

class wolf(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Wolf'
        self.health = 37 * self.level
        self.attack = np.random.randint(8,10) * self.level
        self.defense = np.random.randint(3,5) * self.level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class skeleton(basic_enemy):
    scimitar = item.offensive('Scimitar', 'One handed sword, commonly used by the undead', 0, np.random.randint(7,10))
    thick_bones = item.defensive('Thick Bones', 'This animated skeletons bones are more dense and stronger than normal bones.', 0, np.random.randint(5,8))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Skeleton'
        self.items = [self.scimitar, self.thick_bones]
        self.health = 45 * self.level
        self.attack = self.scimitar.dmg * self.level
        self.defense = self.thick_bones.armor * self.level

    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class spider(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Poisonous Spider'
        self.health = 35 * self.level
        self.attack = np.random.randint(5,9) * self.level
        self.defense = np.random.randint(1,8) * self.level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class bear(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Enraged Bear'
        self.health = 50 * self.level
        self.attack = np.random.randint(10,12) * self.level
        self.defense = np.random.randint(5,8) * self.level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 2 Enemies ####

class wisp(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Wisp'
        self.health = 120 * self.level
        self.attack = np.random.randint(10,16) * self.level
        self.defense = np.random.randint(15,21) * self.level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class possessed_knight(basic_enemy):
    void_greatsword = item.offensive('Void Greatsword', 'A two-handeded sword tainted by the void.', 0, np.random.randint(30,36))
    corrupted_armor = item.defensive('Corrupted Armor', 'Heavy armor worn by knights. This armor has been tainted by the void.', 0, np.random.randint(50,61))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Possessed Knight'
        self.items = [self.void_greatsword, self.corrupted_armor]
        self.health = 200 * self.level
        self.attack = self.void_greatsword.dmg * self.level
        self.defense = self.corrupted_armor.armor * self.level
            
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class elf_bandit(basic_enemy):
    elven_bow = item.offensive('Elven Bow', 'Finely crafted bow made and used commonly by elves.', 0, np.random.randint(35, 41))
    elven_armor = item.defensive('Elven Armor', 'Finely crafted light armor, made by, and commonly worn by Elven warriors.', 0, np.random.randint(30,36))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Elf Bandit'
        self.items = [self.elven_bow, self.elven_armor]
        self.health = 140 * self.level
        self.attack = self.elven_bow.dmg * self.level
        self.defense = self.elven_armor.armor * self.level
            
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class orc_bandit(basic_enemy):
    war_axe = item.offensive('War Axe', 'One handed axe commonly used by orc warriors.', 0, np.random.randint(35, 46))
    orc_armor = item.defensive('Orc Armor', 'Medium armor crafted by and used by orc warriors. Provides decent protection while allowing good movement.', 0, np.random.randint(35, 41))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)        
        self.name = 'Orc Bandit'
        self.items = [self.war_axe, self.orc_armor]
        self.health = 180 * self.level
        self.attack = self.war_axe.dmg * self.level
        self.defense = self.orc_armor.armor * self.level
            
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class goblin(basic_enemy):
    weathered_shortsword = item.offensive('Weathered Shortsword', 'Old and worn shortsword.', 0, np.random.randint(20, 26))
    raggedy_clothes = item.defensive('Raggedy Clothes', 'Old, smelly, trashy garments. Does not offer much protection.', 0, np.random.randint(15,21))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Goblin'
        self.items = [self.weathered_shortsword, self.raggedy_clothes]
        self.health = 110 * self.level
        self.attack = self.weathered_shortsword.dmg * self.level
        self.defense = self.raggedy_clothes.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 3 Enemies ####

class animated_armor(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Animated Armor'
        self.health = 200 * self.level
        self.attack = np.random.randint(25,31) * self.level
        self.defense = np.random.randint(40,51) * self.level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class shield_guardian(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Shield Guardian'
        self.health = 250 * self.level
        self.attack = np.random.randint(20,36) * self.level
        self.defense = np.random.randint(45,56) * self.level

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class guard(basic_enemy):
    halberd = item.offensive('Halberd', 'Basic halberd, used by the common guard in many cities.', 0, np.random.randint(35, 46))
    tower_shield = item.defensive('Tower Shield', 'Very large and heavy shield, commonly used by basic guards in many cities. Who knows how they manage to wield a halberd at the same time...', 0, np.random.randint(50, 66))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Corrupt Guard'
        self.items = [self.halberd, self.tower_shield]
        self.health = 150 * self.level
        self.attack = self.halberd.dmg * self.level
        self.defense = self.tower_shield.armor * self.level

    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class shady_figure(basic_enemy):
    poison_dagger = item.offensive('Poison Dagger', 'Expensive looking dagger with what looks like a mechanism to release poison once the blade is in the victim', 0, np.random.randint(25,31))
    armored_cloak = item.defensive('Armored Cloak', 'Fancy cloak with a strong armor like material weaved into the fabric.', 0, np.random.randint(34,41))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Shady Figure'
        self.items = [self.poison_dagger, self.armored_cloak]
        self.health = 125 * self.level
        self.attack = self.poison_dagger.dmg * self.level
        self.defense = self.armored_cloak.armor * self.level

    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class soulless_aristocrat(basic_enemy):
    fancy_cutlass = item.offensive('Fancy Cutlass', 'An expensive and finely crafted one-handed sword.', 0, np.random.randint(40,46))
    fancy_armor = item.defensive('Fancy Armor', 'Expensive and finely crafted armor, covered unnecessarily in gems.', 0 , np.random.randint(50, 61))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Soulless Aristocrat'
        self.items = [self.fancy_cutlass, self.fancy_armor]
        self.health = 135 * self.level
        self.attack = self.fancy_cutlass.dmg * self.level
        self.defense = self.fancy_armor.armor * self.level

    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')

    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 4 Enemies ####

class troll(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Frost Troll'
        self.health = 265 * self.level
        self.attack = np.random.randint(30, 36) * self.level
        self.defense = np.random.randint(35, 46) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

class mountain_warrior(basic_enemy):
    battle_axe = item.offensive('Battle Axe', 'A two-handed weapon that requires a lot of strength to wield. Devastating to be hit by.', 0, np.random.randint(50,56))
    giant_hide = item.defensive('Giants Hide', 'A lethery type of armor made out of the thick skin of slain giants. Beware whoever is wearing such armor.', 0, np.random.randint(60,71))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Mountain Warrior'
        self.items = [self.battle_axe, self.giant_hide]
        self.health = 245 * self.level
        self.attack = self.battle_axe.dmg * self.level
        self.defense = self.giant_hide.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class hermit(basic_enemy):
    cane = item.offensive('Hermits Cane', 'It looks like a basic old cane... but wielding it makes you feel stronger.', 0, np.random.randint(45, 51))
    bone_armor = item.defensive('Bone Armor', 'Enchanted armor made from the bones of the dead.', 0, np.random.randint(60, 66))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Deranged Hermit'
        self.items = [self.cane, self.bone_armor]
        self.health = 230 * self.level
        self.attack = self.cane.dmg * self.level
        self.defense = self.bone_armor.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class sorcerer(basic_enemy):
    sourcerers_staff = item.offensive("Sorcerer's Staff", 'What looks like just a long stick, is actually a conduit used to cast powerful spells.', 0, np.random.randint(30,41))
    void_cloak = item.defensive('Void Cloak', 'A cloak tainted by the void. Dark power emanates from the fabric.', 0, np.random.randint(50,61))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Dark Sorcerer'
        self.items = [self.sourcerers_staff, self.void_cloak]
        self.health = 210 * self.level
        self.attack = self.sourcerers_staff.dmg * self.level
        self.defense = self.void_cloak.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
#### Village 5 Enemies ####

class kobold(basic_enemy):
    spear = item.offensive('Spear', 'A well made but basic spear. Good for poking things from a distance.', 0, np.random.randint(45, 56))
    scales = item.defensive('Scales', 'Small but hard scales cover the body from head to toe, providing natural armor and decent protection.', 0, np.random.randint(40,46))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Kobold'
        self.items = [self.spear, self.scales]
        self.health = 270 * self.level
        self.attack = self.spear.dmg * self.level
        self.defense = self.scales.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class banshee(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Banshee'
        self.health = 265 * self.level
        self.attack = np.random.randint(30, 36) * self.level
        self.defense = np.random.randint(35, 51) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class crab(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Giant Crab'
        self.health = 325 * self.level
        self.attack = np.random.randint(25, 36) * self.level
        self.defense = np.random.randint(50, 66) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class shapeshifter(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Shapeshifter'
        self.health = np.random.randint(210, 301) * self.level
        self.attack = np.random.randint(25, 46) * self.level
        self.defense = np.random.randint(40, 56) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class lake_dweller(basic_enemy):
    spear_gun = item.offensive('Spear Gun', 'Fires shortened spears at a high velocity. Harder to shoot than a crossbow but capable of dealing much more damage.', 0, np.random.randint(50,56))
    leather_armor = item.defensive('Leather Armor', 'Light armor made from the hides of dead animals.', 0, np.random.randint(40, 46))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Lake Dweller'
        self.items = [self.spear_gun, self.leather_armor]
        self.health = 235 * self.level
        self.attack = self.spear_gun.dmg * self.level
        self.defense = self.leather_armor.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
class water_devil(basic_enemy):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Water Devil'
        self.health = 210 * self.level
        self.attack = np.random.randint(40, 46) * self.level #(1.0 + level/10)
        self.defense = np.random.randint(30,41) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

######## Mini Bosses ########

class mini_boss():
    def __init__(self, level = None, effects = None, abilites = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        self.level = 1
        self.effects = []
        self.abilities = {}
        self.death_exp = 50
        self.base_gold_drop = 100
        self.gold_drop_mult = 1.0 + self.level/10

    def calc_gold_drop(self):
        return (self.base_gold_drop*(self.gold_drop_mult+1.5)) + self.level
    
    def display_abilities(self):
        for i in range(0, len(self.abilities)):
            self.abilities[i].display()
            print('\n')

    def battle_display(self):
        for i in range(0, len(self.abilities)):
            self.abilities[i].battle_display()
            print('\n')

    def info(self):
        print('Level:', self.level)

#### Village 1 Mini Boss ####

class mother_of_wolves(mini_boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Mother of Wolves'
        self.health = 100 * self.level
        self.attack = np.random.randint(18,22) * self.level
        self.defense = np.random.randint(30,35) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 2 Mini Boss ####

class warchief(mini_boss):
    beheader = item.offensive('Beheader', 'A special battle axe hand crafted by the greatest orc blacksmith specifically for the Warchief.', 0, np.random.randint(25, 28))
    warchief_armor = item.defensive('Warchief Armor', 'Special armor hand crafted by the orcs greatest blacksmith. This armor is worn by the warchief.', 0, np.random.randint(33, 37))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Bandit Warchief'
        self.items = [self.beheader, self.warchief_armor]
        self.health = 150 * self.level
        self.attack = self.beheader.dmg * self.level
        self.defense = self.warchief_armor.armor * self.level
            
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 3 Mini Boss ####

class centurion(mini_boss):
    centurion_hammer = item.offensive('Centurion Hammer', 'A sledgehammer crafted from dwarven metal specifically for dwarven constructs.', 0, np.random.randint(29,32))
    metal_body = item.defensive('Metal Body', 'The body of this construct is made completely out of dwarven metal.', 0, np.random.randint(38, 41))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Dwarven Centurion'
        self.items = [self.centurion_hammer, self.metal_body]
        self.health =200 * self.level
        self.attack = self.centurion_hammer.dmg * self.level
        self.defense = self.metal_body.armor * self.level
            
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
        
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 4 Mini Boss ####

class giant(mini_boss):
    royal_club = item.offensive('Royal Club', 'A massive club passed down through generations in the royal family of the giant race.', 0, np.random.randint(30, 34))
    thick_skin = item.defensive('Thick Skin', 'Giants do not really wear armor. Their skin is extremly thick and almost impenetrable.', 0, np.random.randint(40,43))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Royal Giant'
        self.items = [self.royal_club, self.thick_skin]
        self.health = 250 * self.level
        self.attack = self.royal_club.dmg * self.level
        self.defense = self.thick_skin.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
#### Village 5 Mini Boss ####

class cultist_leader(mini_boss):
    void_staff = item.offensive('Void Staff', 'Wooden staff used as a conduit to cast powerful spells. This staff is tainted by the void, giving it strong but dark power.', 0, np.random.randint(35, 39))
    void_robe = item.defensive('Void Robe', 'Enchanted robe tainted by the void. Dark energy emenates.', 0, np.random.randint(44, 48))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Cultist Leader'
        self.items = [self.void_staff, self.void_robe]
        self.health = 300 * self.level
        self.attack = self.void_staff.dmg * self.level
        self.defense = self.void_robe.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
######## Bosses ########

class boss():
    def __init__(self, level = None, effects = None, abilites = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        self.level = 1
        self.effects = []
        self.abilities = {}
        self.death_exp = 100
        self.base_gold_drop = 100
        self.gold_drop_mult = 1.0 + self.level/10
    
    def calc_gold_drop(self):
        return (self.base_gold_drop*(self.gold_drop_mult+2.0)) + self.level
    
    def display_abilities(self):
        for i in range(0, len(self.abilities)):
            self.abilities[i].display()
            print('\n')
            
    def battle_display(self):
        for i in range(0, len(self.abilities)):
            self.abilities[i].battle_display()
            print('\n')

    def info(self):
        print('Level:', self.level)
        
#### Village 1 Boss ####

class revenant(boss):
    revenant_sword = item.offensive('Revenant Sword', 'A greatsword made from the void. Only the darkest of beings can wield this powerful weapon.', 0, np.random.randint(18, 21))
    revenant_armor = item.defensive('Revenant Armor', 'Armor created from the void. You can see the evil emenating from the surface of the armor.', 0, np.random.randint(30,34))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Revenant'
        self.items = [self.revenant_sword, self.revenant_armor]
        self.health = 150 * self.level
        self.attack = self.revenant_sword.dmg * self.level
        self.defense = self.revenant_armor.armor * self.level
        
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        
#### Village 2 Boss ####

class war_machine(boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'War Machine'
        self.health = 200 * self.level
        self.attack = np.random.randint(26, 30) * self.level
        self.defense = np.random.randint(36, 41) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 3 Boss ####

class greed_demon(boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Embodiment of Greed'
        self.health = 250 * self.level
        self.attack = np.random.randint(31, 35) * self.level
        self.defense = np.random.randint(42, 46) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 4 Boss ####

class monstrosity(boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Flesh Monstrosity'
        self.health = 300 * self.level
        self.attack = np.random.randint(36, 40) * self.level
        self.defense = np.random.randint(47, 51) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Village 5 Boss ####

class hydra(mini_boss):
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'Hydra'
        self.health = 350 * self.level
        self.attack = np.random.randint(42, 46) * self.level
        self.defense = np.random.randint(50, 55) * self.level
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

#### Final Boss ####

class world_breaker(boss):
    the_reckoning = item.offensive('The Reckoning', 'One of the ancient weapons thought to be crafted by celestials. Originally belonged to one of the original founders of the 2 kingdoms and passed down through rulers.', 0, np.random.randint(50,55))
    demon_hide = item.defensive('Demon Hide', 'Demonic energy has completely taken over the body, creating a sort of dark armor.', 0, np.random.randint(60,65))
    def __init__(self, name = None, level = None, health = None, attack = None, defense = None, effects = None, abilities = None, items = None, death_exp = None, base_gold_drop = None, gold_drop_mult = None):
        super().__init__(level, effects, abilities, death_exp, base_gold_drop, gold_drop_mult)
        self.name = 'World Breaker'
        self.items = [self.the_reckoning, self.demon_hide]
        self.health = 400 * self.level
        self.attack = self.the_reckoning.dmg * self.level 
        self.defense = self.demon_hide.armor * self.level
            
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Enemy:', self.name)
        super().info()
        print('Health:', self.health)
        print('Attack:', self.attack)
        print('Defense:', self.defense)

###############################################################################

############################ PLAYER CHARACTER SETUP ############################

class player_setUp: # Base class for setting up a character
    def __init__(self, name, race, effects = None, curr_exp = None, needed_exp = None, level = None, abilities = None, items = None, gold = None):
        self.name = name
        self.race = race
        self.abilities = {'Heal':ability.heal, 'Barrier':ability.barrier}
        self.effects = []
        self.items = []
        self.gold = 0
        self.curr_exp = 0
        self.needed_exp = 100
        self.level = 1
        
    def display_abilities(self):
        for i in self.abilities:
            self.abilities[i].display()
            print('\n')
            
    def battle_display(self):
        for i in self.abilities:
            self.abilities[i].battle_display()
            print('\n')
            
    def display_items(self):
        for i in self.items:
            i.display()
            print('\n')
            
    def info(self):
        print('Name:', self.name)
        print('Race:', self.race)
        print('Gold:', self.gold)
        print('Experience: {}/{}'.format(self.curr_exp, self.needed_exp))
        print('Level:', self.level)
        
    def level_up(self):
        self.level += 1
        self.max_health += 5
        self.health += 5
        self.max_mana += 5
        self.dmg_mult += 0.1
        
        if self.level in [2,3,4,5,6,8,9,12]: # example look: locked_abilities = [meteor_shower, winter_beam, acid_spores, hail, impale, revitalize, daing_bolt, short_circuit]
            new_ability = self.locked_abilities.pop()
            self.abilities[new_ability.name] = new_ability
            print("You've unlocked a new ability! New Ability:", new_ability.name)
        
class mage(player_setUp): 
    def __init__(self, name, race, player_class, locked_abilities, health = None, max_health = None, mana = None, max_mana = None, dmg_mult = None, attack = None, defense = None, effects = None, curr_exp = None, needed_exp = None, level = None, abilities = None, items = None, gold = None):
        super().__init__(name, race, abilities, effects, items, gold, curr_exp, needed_exp, level)
        self.player_class = player_class
        self.locked_abilities = locked_abilities
        self.health = 100
        self.max_health = 100
        self.mana = 120
        self.max_mana = 120
        self.dmg_mult = 1.0
        self.attack = 0
        self.defense = 0
        
    def info(self):
        super().info()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
    
class warrior(player_setUp):
    def __init__(self, name, race, player_class, locked_abilities, health = None, max_health = None, mana = None, max_mana = None, dmg_mult = None, attack = None, defense = None, effects = None, curr_exp = None, needed_exp = None, level = None, abilities = None, items = None, gold = None):
        super().__init__(name, race, abilities, effects, items, gold, curr_exp, needed_exp, level)
        self.player_class = player_class
        self.locked_abilities = locked_abilities
        self.health = 120
        self.max_health = 120
        self.mana = 80
        self.max_mana = 80
        self.dmg_mult = 1.0
        self.attack = 0
        self.defense = 0
        
    def info(self):
        super().info()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
    
class rogue(player_setUp):
    def __init__(self, name, race, player_class, locked_abilities, health = None, max_health = None, mana = None, max_mana = None, dmg_mult = None, attack = None, defense = None, effects = None, curr_exp = None, needed_exp = None, level = None, abilities = None, items = None, gold = None):
        super().__init__(name, race, abilities, effects, items, gold, curr_exp, needed_exp, level)
        self.player_class = player_class
        self.locked_abilities = locked_abilities
        self.health = 80
        self.max_health = 80
        self.mana = 100
        self.max_mana = 100
        self.dmg_mult = 1.1
        self.attack = 0
        self.defense = 0

    def info(self):
        super().info()
        print('Class:', self.player_class)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Attack:', self.attack)
        print('Defense:', self.defense)
        print('\n')
        
################################################################################
