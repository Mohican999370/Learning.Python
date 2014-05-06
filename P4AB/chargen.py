__author__ = 'Son-Huy TRAN'
__version__ = 0.1
"""
chargen.py
Problem: Generate a description for a fantasy role-playing character.
Target Users: Me and my friends
Target System: GNU/Linux
Interface: Command-line
Functional Requirements: Print out the character sheet
User must be able to input the character's
name, description, gender and race
Testing: Simple run test
Maintainer: maintainer@website.com
"""

Name = ""
Desc = ""
Gender = ""
Race = ""

# Prompt user for user-defined information
Name = input('What is your Name? ')
Desc = input('Describe yourself: ')
Gender = input('What Gender are you? (male / female / unsure): ')
Race = input('What fantasy Race are you? (Pixie / Vulcan / Gelfling / Troll): ')

# Output the character sheet
fancy_line = "<~~==|#|==~~++**\@/**++~~==|#|==~~>"
print("\n", fancy_line)
print("\t", Name)
print("\t", Race, Gender)
print("\t", Desc)
print(fancy_line, "\n")