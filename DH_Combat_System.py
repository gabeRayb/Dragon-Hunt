"""
Authors: Johnnie Clark, Gabriel Rayburn

Project Name: Dragon Hunt

This file holds the classes used for the combat system.
"""
import DH_Abilities as abilities
############################### BATTLE SYSTEM ###############################
def attack(attacker, defender):
    pass

def run_away():
    pass

def use_ability(target, source, ability):
    if isinstance(ability,abilities.offensive):
        target.health -= dmg_calc(target, source, ability)
    # elif isinstance(ability,abilities.defensive):
    #     source

def dmg_calc(target,ability,source):
    return ((ability.dmg * source.dmg_mult) + source.attack) - ((target.defense/200)*ability.dmg)

#############################################################################