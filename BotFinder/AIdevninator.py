from random import randint

# assignement des variables
# variante : numberToFind = int(input("\n Quelle nombre je dois deviner ? "))
numberToFind = randint(1,100)
testNumber = 50
LowLimit = 1
HightLimit =100
essaie = 0

# lancement du jeux
print("\n","Le nombre a trouver est : ",numberToFind, "\n")

# script qui trouve le nombre
while True : 

    if numberToFind < testNumber : 
        essaie += 1
        HightLimit = testNumber
        testNumber = int(HightLimit/2)
        print("je test : ", testNumber)

    elif numberToFind > testNumber : 
        essaie += 1
        LowLimit = testNumber
        testNumber = int((LowLimit + HightLimit) /2)
        print("je test : ",testNumber)

    else : 
        print("\n","j'ai gagné en ", essaie, " tentatives")
        break 