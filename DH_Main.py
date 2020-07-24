"""
Authors: Johnnie Clark, Gabriel Rayburn

Project Name: Dragon Hunt

This file is where the game will be ran from. 
"""

import DH_Character_Creation as character
#import DH_Combat_System as battle

#play = False
    
# intro = """"""
# print(intro)

print('\nWelcome to Dragon Hunt!\n')
#while play:
    
name = input('Enter character name (10 characters max): ')

while len(name) > 10:
    print('\nThats more than 10 characters...')
    name = input('Enter character name (10 characters max): ')
    
race = input('Enter the race of your character: ').capitalize()

pClass = input('What class would you like to play as? (Warrior, Mage, Rogue): ').capitalize()

while pClass != 'Warrior' and pClass != 'Mage' and pClass != 'Rogue':
    print('\nNot a valid class.')
    pClass = input('Please type one of the 3 avaliable classes (Warrior, Mage, Rogue): ').capitalize()
    
print('\n')

if pClass == 'Warrior':
    p1 = character.warrior(name, race, pClass)
    
if pClass == 'Mage':
    p1 = character.mage(name, race, pClass)
    
if pClass == 'Rogue':
    p1 = character.rogue(name, race, pClass)
    
p1.print_stats()

