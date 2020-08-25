"""
Created on Fri Aug  7 11:41:29 2020

Authors: Johnnie Clark, Gabriel Rayburn
"""

import sys
import os
import DH_Character_Creation as character
import DH_Combat_System as battle
from os import system,name
import DH_Items as items
import DH_Random_Events as rand_events
import DH_Abilities as abilities


#Clear the screen ------->From: https://www.geeksforgeeks.org/clear-screen-python/ <-------------
def clr():
    
    #if os used is windows
    if name == 'nt':
        return system('cls')
    
    #if os used is mac of linux
    else:
        return system('clear')

############################## TITLE SCREEN ##############################

def title_selections(): # function to take the input from the user
    choice = input('> ').capitalize()
    if choice == 'Start':
        start_game()
    elif choice == 'Help':
        help_menu()
    elif choice == 'Quit':
        sys.exit()
    while choice not in ['Start', 'Help', 'Quit']: # redisplay options if incorrect option is given by the user
        print('Please choose a valid option')
        choice = input('> ').capitalize()
        if choice == 'Start':
            start_game()
        elif choice == 'Help':
            help_menu()
        elif choice == 'Quit':
            sys.exit()

def title_screen(): # display the title screen for the user
    clr()
    print('###########################')
    print('# Welcome to Dragon Hunt! #')
    print('###########################')
    print('          - Start -')
    print('          - Help -')
    print('          - Quit -')
    title_selections()

def help_menu(): # display the help menu for the user
    print('###########################')
    print('# Welcome to Dragon Hunt! #')
    print('###########################')
    print('- Type the action you want to make when prompted -')
    title_selections()
    
############################## RUNNING THE GAME ##############################

def game_intro():
    print('')
    
def create_character():
    name = input('Enter character name (10 characters max): ')

    while len(name) > 10:
        print('\nThats more than 10 characters...')
        name = input('Enter character name (10 characters max): ')
        
    race = input('Enter the race of your character (10 characters max): ').capitalize()
    
    while len(race) > 10:
        print('\nThats more than 10 characters...')
        race = input('Enter the race of your character (10 characters max): ').capitalize()
    
    player_class = input('What class would you like to play as? (Warrior, Mage, Rogue): ').capitalize()
    
    while player_class != 'Warrior' and player_class != 'Mage' and player_class != 'Rogue':
        print('\nNot a valid class.')
        player_class = input('Please type one of the 3 avaliable classes (Warrior, Mage, Rogue): ').capitalize()
    
    print('\n')
    
    if player_class == 'Warrior':
        player = character.warrior(name, race, player_class)
        
    if player_class == 'Mage':
        player = character.mage(name, race, player_class)
        
    if player_class == 'Rogue':
        player = character.rogue(name, race, player_class)
    
    clr()
    player.info()
    return player

def start_game():
    game_intro()
    player = create_character()
    if isinstance(player,character.mage):
        print("Here is a wand to start your journey.")
        player.items.append(items.wand)
        print("You received a wand!")
        print("Items:")
        player.display_items()
        print("Here is a spell to start your journey.")
        player.abilities.append(abilities.fireball)
        print("You learned the Fireball ability!")
        print("Abilities:")
        player.display_abilities()
        
    event = rand_events.roll_event()
    