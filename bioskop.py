#cinema repertoire#

############################################

'''
@author Aleksandar Gajic
        alexandar0702@gmail.com
        created date: 12.05.2022
'''

############################################


bioskopi = {
    "b1":{ 
        "naziv":"Cineplex",  
        "adresa":"Jurija Gagarina 45" 
    },
    "b2":{
        "naziv":"Tuckwood",  
        "adresa":"Kneza Milosa 1" 
    } 
}
ob = input("Odaberi bioskop: ") 
print(bioskopi[ob]["naziv"],bioskopi[ob]["adresa"]) 

for b in bioskopi:
    print(bioskopi[b]["naziv"],bioskopi[b]["adresa"])


    #   IN PROGRESS  #