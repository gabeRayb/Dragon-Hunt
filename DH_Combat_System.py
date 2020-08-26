"""
Authors: Johnnie Clark, Gabriel Rayburn

Project Name: Dragon Hunt

This file holds the classes used for the combat system.
"""
import DH_Abilities as abilities
import numpy as np
import DH_Title_Screen as ts
############################### BATTLE SYSTEM ###############################
def battle(player, event):
    ts.clr()
    event.display()
    event.enemy.info()
    print()
    player.info()
    print()
    
    while player.health > 0 and event.enemy.health > 0:
        print("If you want to try running away, type 'run'. Otherwise,\n")
        #Player attacks
        print("Choose an ability:")
        player.display_abilities()
        ability_key = input(">").capitalize()
        valid = False
        while not valid: #check if input is valid
            ts.clr()
            if ability_key == 'Run' or ability_key == 'R':
                valid = True
                if run_away():
                    print("You successfully escaped!")
                    return
                else:
                    print("You couldn't escape, unfortunate..")
                    
            elif player.abilities.get(ability_key) == None: 
                print("That is not a valid input, please choose one of your abilities or try running.")
                valid = False
                continue
            
            else: 
                valid = True
                dmg = dmg_calc(event.enemy, player.abilities[ability_key], player)
                use_ability(event.enemy, player, player.abilities[ability_key])
                print(f"You did {dmg} damage to the {event.enemy.name}!")
        
            if event.enemy.health <= 0:
                continue
        enemy_dmg = enemy_dmg_calc(player,event.enemy)
        player.health -= enemy_dmg
        print(f"The {event.enemy.name} attacked you, dealing {enemy_dmg} damage!")
        
        
        
        
    if event.enemy.health <= 0:
        if player.currExp + event.enemy.death_exp >= 100:
            extra = player.experience + event.enemt.death_exp - 100
            player.levelUp()
            player.currExp = extra
        player.gold += event.enemy.base_gold_drop * event.enemy.gold_drop_mult    
        return print(f"Victory! You were rewarded {event.enemy.base_gold_drop*event.enemy.gold_drop_mult} and {event.enemy.death_exp} experience.")
    
    else:
        print("You died. Better luck next time..")
        return ts.title_screen()
    
    
def run_away():
    if np.randint(0,100) <= 34: return True
    else: return False

def use_ability(target, source, ability):
    if isinstance(ability,abilities.offensive):
        target.health -= dmg_calc(target, ability, source)
    # elif isinstance(ability,abilities.defensive):
    #     source

def dmg_calc(target,ability,source):
    return ((ability.dmg * source.dmg_mult) + source.attack) - ((target.defense/200)*ability.dmg)

def enemy_dmg_calc(target,source):
    return source.attack - ((target.defense/200)*source.attack)
#############################################################################