#UPGRADE COMPUTER CONGIGURATION WITH FILTER#

#############################################

'''
@author Aleksandar Gajic
        alexandar0702@gmail.com
        created date: 12.05.2022
'''

#############################################

from http.server import executable
import time


processoramd1        = int(170.00) and str("Ryzen 3(3200G)")
processoramd2        = int(190.00) and str("Ryzen 5(5600X)")
processorintel1      = int(298.00) and str("Intel Core I7 10700K") 
processorintel2      = int(989.00) and str("Intel Core I9 7900X")

ram1                 = int(50.00) and str("16")
ram2                 = int(30.00) and str("8")

ssd1                 = int(70.00) and str("500")
ssd2                 = int(40.00) and str("250")

graphic1             = int(579.00) and str("AMD Radeon RX 6800")
graphic2             = int(499.00) and str("NVIDIA GeForce RTX 3070")

hdd                  = int(40.00) and str("1000")




print("Upgrade Computer Filter")
print("=======================")
time.sleep(1)

print("Choose your components")
time.sleep(1)


#processor
inputprocess = str(input("Processor(AMD/Intel): "))
if inputprocess == "amd":
    inputamd = str(input(" AMD Ryzen(3/5): "))
    if inputamd == "3":
        print ("  Processor is: ", str(processoramd1))
    elif inputamd == "5":
        print ("  Processor is: ", str(processoramd2))
    else: print("That processor does not exist, start filter again!"), exit()


    
elif inputprocess == "intel":
    inputintel = str(input(" Intel Core(I7/I9): "))
    if inputintel == "i7":
        print ("  Processor is: ", str(processorintel1))
    elif inputintel == "i9":
        print ("  Processor is: ", str(processorintel2))
    else: print("That processor does not exist, start filter again!"), exit()
else: print("That processor does not exist, start filter again!"), exit()



#ram memory
inputram = str(input("RAM Memory(16/8)GB:"))
if inputram == "16":
    print(" RAM Memory is: ", ram1, "GB")

elif inputram =="8":
    print(" RAM Memory is: ", ram2, "GB")

else: print("That RAM does not exist, start filter again!"), exit()



#ssd/hdd memory
inputmemory = str(input("SSD/HDD Memory: "))
if inputmemory == "ssd":
    inputssd = str(input(" SSD(500/250)GB: "))
    if inputssd == "500":
        print("  SSD Memory is: ", ssd1, "GB")
    elif inputssd == "250":
        print("  SSD Memory is: ", ssd2, "GB")
    else: print("That SSD does not exist, start filter again!"), exit()
elif inputmemory == "hdd":
    print(" HDD(one option) is: ", hdd, "GB")
else: print("That Memory does not exist, start filter again!"), exit()
   


#graphic
inputgraph = str(input("Graphic Card(NVIDIA/AMD): "))
if inputgraph == "nvidia":
    print("Graphic card is: ", graphic2)

elif inputgraph == "amd":
    print("Grapchic card is: ", graphic1)

else: print("That Graphic Card does not exist, start filter again!"), exit()


print("You have finished with choosing components!")
print("=======================")

time.sleep(2)
print ("Loading, please wait...")
time.sleep(3)
print ("Searching for a near store with these upgrade components...  ")
time.sleep(5)
print("The nearest store is in Belgrade: 'Tech shop' Belgrade 11000, +38162567891")
time.sleep(1)
print("You have finished, Thank you for searching!")
print("=======================")


    #    DONE   #