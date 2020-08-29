"""
Authors: Johnnie Clark, Gabriel Rayburn

Project Name: Dragon Hunt

This file holds the classes used for the combat system.
"""
import numpy as np
import DH_Abilities as abilities
import DH_Title_Screen as ts
############################### BATTLE SYSTEM ###############################

def battle(player, event):
    temp_health = 0
    temp_defense = 0
    ts.clr()
    event.display()
    event.enemy.info()
    print()
    player.info()
    print()
    
    while player.health > 0 and event.enemy.health > 0:
        
        valid = False
        #check if input is valid
        while not valid: 
            print("If you want to try running away, type 'run'. Otherwise,\n")
            print("Choose an ability:")
            player.display_abilities()
            ability_key = input(">").capitalize()
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
            elif player.abilities[ability_key].r_cost > player.mana:
                # use_ability(event.enemy, player, player.abilities[ability_key]) == False:
                valid = False
                print("You don't have enough mana!")
                continue
            else: 
                if isinstance(player.abilities[ability_key],abilities.offensive):
                    valid = True
                    dmg = dmg_calc(event.enemy, player.abilities[ability_key], player)
                    use_ability(event.enemy, player, player.abilities[ability_key], temp_health, temp_defense)
                    info = f"You did {dmg} damage to the {event.enemy.name}!"
                else:
                    valid = True
                    use_ability(event.enemy, player, player.abilities[ability_key], temp_health, temp_defense)
                    if player.abilities[ability_key].stat == "Health":
                        info = f"You restored {player.abilities[ability_key].val} health points!"
                    elif player.abilities[ability_key].stat == "Max Health":
                        info = f"You increased your max health by {player.abilities[ability_key].val}!"
                    elif player.abilities[ability_key].stat == "Defense":
                        info = f"You increased your defense by {player.abilities[ability_key].val}!"
        
        if event.enemy.health <= 0:
            continue
        enemy_dmg = enemy_dmg_calc(player, event.enemy)
        player.health -= enemy_dmg
        ts.clr()
        event.enemy.info()
        print()
        player.info()
        print(info)
        print(f"The {event.enemy.name} attacked you, dealing {enemy_dmg} damage!")
        
        
    input("Type anything to continue.")    
    ts.clr()    
    if event.enemy.health <= 0:
        if player.curr_exp + event.enemy.death_exp >= player.needed_exp:
            extra = player.curr_exp + event.enemy.death_exp - player.needed_exp
            player.level_up()
            player.curr_exp = extra
        else:
            player.curr_exp += event.enemy.death_exp
        player.gold += event.enemy.base_gold_drop * event.enemy.gold_drop_mult    
        print(f"Victory! You were rewarded {event.enemy.base_gold_drop*event.enemy.gold_drop_mult} and {event.enemy.death_exp} experience.")
        return input("Press enter to continue.")
    
    else:
        print("You died. Better luck next time..")
        input("Press enter to continue.")
        return ts.title_screen()
    
    
def run_away():
    if np.random.randint(0,100) <= 34: return True
    else: return False

def use_ability(target, source, ability, temp_health, temp_defense):
    if isinstance(ability,abilities.offensive):
        target.health -= dmg_calc(target, ability, source)
        source.mana -= ability.r_cost
    elif isinstance(ability,abilities.defensive):
        source.mana -= ability.r_cost
        #Abilities that heal
        if ability.stat == "Health":
            #Caps the heal at sources max health
            if (source.health + ability.val) > source.max_health:
                heal = ability.val - ((source.health + ability.val) - source.max_health)
            else:
                heal = ability.val
            source.health += heal
        #Abilities that increase max health
        elif ability.stat == "Max Health":
            # temp_health += ability.val
            source.max_health += ability.val
            source.health += ability.val
        #Abilities that increase defense
        elif ability.stat == "Defense":
            # temp_defense += ability.val
            source.defense += ability.val

def dmg_calc(target,ability,source):
    return ((ability.dmg * source.dmg_mult) + source.attack) - ((target.defense/200)*ability.dmg)

def enemy_dmg_calc(target,source):
    return source.attack - ((target.defense/200)*source.attack)
#############################################################################