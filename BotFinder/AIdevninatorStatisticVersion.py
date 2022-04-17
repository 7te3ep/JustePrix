import numpy 
from random import randint
import os

# debut du code 

essaiemoyenne = []
indexlaod = 3
laoding = ["laoding...","laoding..","laoding."]

# process

for test in range(1000000):
    numberToFind = randint(1,99)
    testNumber = 50
    LowLimit = 1
    HightLimit =100
    essaie = 0

    # script qui trouve le nombre
    while True : 

        if numberToFind < testNumber : 
            essaie += 1
            HightLimit = testNumber
            testNumber = int(HightLimit/2)
            

        elif numberToFind > testNumber : 
            essaie += 1
            LowLimit = testNumber
            testNumber = int((LowLimit + HightLimit) /2)
            
        else : 
            essaiemoyenne.append(essaie)
            indexlaod = randint(0,2)
            print(laoding[indexlaod])
            MoyenneFinal = numpy.mean(essaiemoyenne)
            break

# affichage de la moyenne final
print(MoyenneFinal)
            