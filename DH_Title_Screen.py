"""
Created on Fri Aug  7 11:41:29 2020
Authors: Johnnie Clark, Gabriel Rayburn
"""

import sys
import DH_Character_Creation as character
import DH_Combat_System as combat_sys
from os import system,name
import DH_Items as item
import DH_Random_Events as rand_event
import DH_Abilities as ability
import copy as copy


#Clear the screen ------->From: https://www.geeksforgeeks.org/clear-screen-python/ <-------
def clr():
    
    #if os used is windows
    if name == 'nt':
        return system('cls')
    
    #if os used is mac of linux
    else:
        return system('clear')

############################## TITLE SCREEN ##############################
# Title Screen -------> From: https://www.youtube.com/watch?v=xHPmXArK6Tg <-------

def title_selections(): # function to take the input from the user
    choice = input('> ').capitalize()
    if choice == 'Start' or choice == 'S':
        start_game()
    elif choice == 'Help' or choice == 'H':
        help_menu()
    elif choice == 'Quit' or choice == 'Q':
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
        print("Here is a wand and some abilities to start your journey.")
        
        player.items.append(item.wand)
        print("You received a wand!")
        print("Items:")
        player.display_items()
        
        player.abilities[ability.fireball.name] = ability.fireball
        print("You learned the Fireball ability!")
        print("Abilities:\n")
        player.display_abilities()
    print(f'''King of Steniara: 
          Greetings {player.name}, I've summoned you here 
          to ask for your aid. The King of Doriona has become corrupted and 
          has taken control of the legendary dragon that lives in that region, 
          Draxduin, in order to gain the power to rule the continent. As you 
          know, Draxduin is the other spiritual half of Parthernax, the dragon 
          that lives in our region. This has caused an imbalance in the world. 
          Please {player.name}, I ask you to travel to the land of Doriona and 
          bring an end to the imbalance!
          
          To get to the Kingom of Doriona, you must travel from village to 
          village slaying the elite guards sent out by Doriona's King to take 
          control of each village. Along the way you will encounter enemies 
          who you need to slay in order to grow stronger and earn gold that 
          you can spend at the village shops once you clear the town of evil.''')
    input("Press enter to start your journey.")    
    for i in range(1,6):
        clr()
        print(f"############## Chapter {i} ##############\n")
        for j in range(1,11):
            print(f"############## Event {j} of 10 ##############")
            player.mana = copy.copy(player.max_mana)#refill mana before event
            print("Your mana was refilled.\n")
            event = rand_event.roll_event(i)
            input("Press enter to continue.")
            combat_sys.battle(player,event)