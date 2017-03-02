"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:
        Generate datasets for question 2
"""

import random

# Generate 500 training examples
fileName500 = "datosP2EM2017/datos_P2_Gen_500.txt"
f500 = open(fileName500, 'w')

for i in range(0, 500):
    # Generate random points within the square
    x = random.uniform(0, 20)
    y = random.uniform(0, 20)

    # Determine whether said point belongs or not to the circle
    ecuation = (x - 10) ** 2 + (y - 10) ** 2
    if  ecuation < 36 or ecuation == 36 :
        isCircle = "1"
    else:
        isCircle = "0"

    f500.write(str(x) + " " + str(y) + " " + isCircle + "\n")


# Generate 1000 training examples
fileName1000 = "datosP2EM2017/datos_P2_Gen_1000.txt"
f1000 = open(fileName1000, 'w')

for i in range(0, 1000):
    # Generate random points within the square
    x = random.uniform(0, 20)
    y = random.uniform(0, 20)

    # Determine whether said point belongs or not to the circle
    ecuation = (x - 10) ** 2 + (y - 10) ** 2
    if  ecuation < 36 or ecuation == 36 :
        isCircle = "1"
    else:
        isCircle = "0"

    f1000.write(str(x) + " " + str(y) + " " + isCircle + "\n")


# Generate 2000 training examples
fileName2000 = "datosP2EM2017/datos_P2_Gen_2000.txt"
f2000 = open(fileName2000, 'w')

for i in range(0, 2000):
    # Generate random points within the square
    x = random.uniform(0, 20)
    y = random.uniform(0, 20)

    # Determine whether said point belongs or not to the circle
    ecuation = (x - 10) ** 2 + (y - 10) ** 2
    if  ecuation < 36 or ecuation == 36 :
        isCircle = "1"
    else:
        isCircle = "0"

    f2000.write(str(x) + " " + str(y) + " " + isCircle + "\n")

fTest = open("datosP2EM2017/dataset_test_circle.txt", 'w')

x = 0
while x < 20:
    y = 0
    while y < 20:
        ecuation = (x - 10) ** 2 + (y - 10) ** 2
        if  ecuation < 36 or ecuation == 36 :
            isCircle = "1"
        else:
            isCircle = "0"

        fTest.write(str(x) + " " + str(y) + " " + isCircle + "\n")
        y += 0.2005
    x += 0.2005
