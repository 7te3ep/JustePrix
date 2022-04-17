from random import randint
import os
os.system('clear')
print("robot : je vien de choisir un nombre en 1 et 100, devine le !")
randomnumber = randint(0,100)

for test in range (10) : 
    devine = input("vous : Je pense que c'est ")
    if int(randomnumber) == int(devine) : 
        print("robot : Vous avez gagner !")
    elif int(randomnumber) > int(devine) : 
        print("robot : mon nombre est plus grand")
    elif int(randomnumber) < int(devine) :
        print("robot : mon nombre est plus petit")
print("Vous n'avez pas trouvé a temps, c'etait ", randomnumber)