#Appearnce and age login#

#############################################

'''
@author Aleksandar Gajic
        alexandar0702@gmail.com
        created date: 12.05.2022
'''

#############################################

login_years = 18

print ("Set you appearance")

input_field = input("Male or female (male/female)?")
if input_field =="male":
    print("You choose male")
else:
    print("You choose female")

my_years = int(input("Now set your age: "))
if my_years >= login_years:
    print("Thanks for login!")
else:
    print("Sorry! But you cannot register because you are under 18 years old.")


    #    DONE   #