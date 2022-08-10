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


    #    TO DO - LOTTO   #    




from crypt import methods
import random

print ("GUESSING NUMBER")

print("Enter number(1-100):")

my_number1   = int(input())
my_number2   = int(input())
my_number3   = int(input())
my_number4   = int(input())
my_number5   = int(input())
my_number6   = int(input())
my_number7   = int(input())


random_number1   = random.randint(1,100)
random_number2   = random.randint(1,100)
random_number3   = random.randint(1,100)
random_number4   = random.randint(1,100)
random_number5   = random.randint(1,100)
random_number6   = random.randint(1,100)
random_number7   = random.randint(1,100)

print("Your number:", my_number1)
print("Your number:", my_number2)
print("Your number:", my_number3)
print("Your number:", my_number4)
print("Your number:", my_number5)
print("Your number:", my_number6)
print("Your number:", my_number7)

print("Computer number:", random_number1)
print("Computer number:", random_number2)
print("Computer number:", random_number3)
print("Computer number:", random_number4)
print("Computer number:", random_number5)
print("Computer number:", random_number6)
print("Computer number:", random_number7)


if my_number1 == random_number1:
    print ("Congratulations. You guessed the number!")
else:
    print ("False. Try again!")