#EXCHANGE EUR AND USD TO RSD#

#############################################

'''
@author Aleksandar Gajic
        alexandar0702@gmail.com
        created date: 19.05.2022
'''

#############################################

eur = 118 #rsd#
usd = 115 #rsd#

print ("| WELCOME TO THE EXCHANGE |")

val = float (input("Enter value (RSD): "))
total_euro = "Total Euro: %.2f" % (val/eur)
total_usd = "Total Usd: %.2f" % (val/usd)

currency = str (input("Set currency: "))

eur = total_euro
usd = total_usd

if currency == "eur":
    print(total_euro)

else:
    print(total_usd)