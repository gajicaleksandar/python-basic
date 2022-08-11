#HIGHSCORE#

############################################

'''
@author Aleksandar Gajic
        alexandar0702@gmail.com
        created date: 12.05.2022
'''

############################################

import random 

najveci_rezultat = random.randint(0,1)
nvr = najveci_rezultat

print ("Unesi broj(0-300):")
nas_rezultat = int(input())
if(nas_rezultat>nvr):
    najveci_rezultat = nas_rezultat
    print("Pobedio si, najveci rezultat je", nvr)
else:
    print("Izgubio si, najveci rezultat je", najveci_rezultat)


    #IN PROGRESS