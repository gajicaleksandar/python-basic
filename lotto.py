#LOTTO GAME#


#############################################

'''
@author Aleksandar Gajic
        alexandar0702@gmail.com
        created date: 09.08.2022
'''

#############################################


import time
from random import randint as rnd


RANGE = 15
DRAWS = 7


def randomise():

    rands = []
    for i in range(DRAWS):
        number = rnd(1,RANGE)
        while number in rands:
            number = rnd(1,RANGE)
        rands.append(number)
    return rands

def drawing():
    draws = []
    for i in range(DRAWS):
        while True:
            try:
                number = int(input(f"Please input number from 1 to {RANGE}: "))
                if number < 1 or number > RANGE:
                    print("Outside the RANGE! Please input number from 1 to {RANGE}: ")
                elif number in draws:
                    print("Number is already drawn! Please input another number from 1 to {RANGE}: ")
                else:
                    break
            except:
                print("Only integer numbers are allowed!")
        draws.append(number) 
    return draws

rands = randomise()
rands.sort()
draws = drawing()
draws.sort()

hits = 0
hitlist = []

for draw in draws:
    if draw in rands:
        hits+=1
        hitlist.append(draw)
        

print("You are finished!")
print("Loading... Please Wait!")
time.sleep(2)
print(f"Lotto numbers: {rands}")
print(f"Your numbers: {draws}")
time.sleep(2)
if hits == 0:
    print("You didn't hit number! ")
elif hits == 1:
    print("You hit 1 number !")
    print(f"One hitted number: {hitlist}")
else: print(f"You hit {hits} numbers !"), print(f"Hitted numbers: {hitlist}")