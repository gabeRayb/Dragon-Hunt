"""
Authors: Johnnie Clark, Gabriel Rayburn

Project Name: Dragon Hunt

This file is where the game will be ran from. 
"""

import DH_Character_Creation as character
import DH_Abilities as abilities
import DH_Random_Events as rand_events
from os import system,name
#import DH_Combat_System as battle

#Clear the screen ------->From: https://www.geeksforgeeks.org/clear-screen-python/ <-------------
def clr():
    
    #if os used is windows
    if name == 'nt':
        return system('cls')
    
    #if os used is mac of linux
    else:
        return system('clear')

    
# intro = """"""
# print(intro)

print('\nWelcome to Dragon Hunt!\n')
#while play:
    
p_name = input('Enter character name (10 characters max): ')

while len(p_name) > 10:
    print('\nThats more than 10 characters...')
    p_name = input('Enter character name (10 characters max): ')
    
race = input('Enter the race of your character: ').capitalize()

pClass = input('What class would you like to play as? (Warrior, Mage, Rogue): ').capitalize()

while pClass != 'Warrior' and pClass != 'Mage' and pClass != 'Rogue':
    print('\nNot a valid class.')
    pClass = input('Please type one of the 3 avaliable classes (Warrior, Mage, Rogue): ').capitalize()
    
print('\n')

if pClass == 'Warrior':
    p1 = character.warrior(p_name, race, pClass)
    
if pClass == 'Mage':
    p1 = character.mage(p_name, race, pClass)
    
if pClass == 'Rogue':
    p1 = character.rogue(p_name, race, pClass)
    
# p1.print_stats()



event = rand_events.roll_event()
# print("\033[H\033[J") 
# print("$([char]27)")
# print('\033[2J')
clr()
event.display()
p1.print_stats()

test = input('Please type one of the 3 avaliable classes (Warrior, Mage, Rogue): ').capitalize()
