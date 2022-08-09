#GUESS NUMBER WITH COMPUTER#

############################################

'''
@author Aleksandar Gajic
        alexandar0702@gmail.com
        created date: 12.05.2022
'''

############################################

from crypt import methods
import random

print ("GUESSING NUMBER")

print("Enter number(1-100):")
my_number   = int(input())
random_number   = random.randint(1,100)
print("Your number:", my_number)
print("Computer number:", random_number)

if my_number == random_number:
    print ("Congratulations. You guessed the number!")
else:
    print ("False. Try again!")


    #    DONE   #