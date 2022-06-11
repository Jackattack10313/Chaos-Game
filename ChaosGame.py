#!/usr/bin/env python3
import random
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
xVals = []
yVals = []


def printMenu():
    print("Welcome to chaos game!")
    print("1. Sierpiński Gasket")
    print("2. Sierpiński Tetrahedron - previous vertex will not be chosen in subsequent iteration")

    selection = 0
    valid = False
    while not valid:
        try:
            selection = int(input("Enter selection: "))
            if 0 < selection < 3:
                valid = True
        except ValueError:
            print("Invalid selection")
    return selection


def main():
    selection = printMenu()

    iterations = 0
    valid = False
    while not valid:
        try:
            iterations = int(input("Enter iterations: "))
            if iterations > 0:
                valid = True
        except ValueError:
            print("Invalid selection")
    # Gasket
    if selection == 1:
        # Weighing the y values towards the bottom (otherwise the points get clumped near the apex - ~50% take up the
        # top half in the vertical direction but not 50% in the volume of the triangle - attempt to get a uniform
        # distribution)
        y = random.triangular(0, 1, 0.25)
        x = random.uniform(y - 1, 1 - y)
        for i in range(iterations):
            # Choosing a random axis
            axis = random.randint(1, 3)
            if axis == 1:
                x += 0.5 * (1 - x)
                y += 0.5 * (0 - y)
            elif axis == 2:
                x += 0.5 * (0 - x)
                y += 0.5 * (1 - y)
            else:
                x += 0.5 * (-1 - x)
                y += 0.5 * (0 - y)
            xVals.append(x)
            yVals.append(y)
    # Tetrahedron
    else:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        previousAxis = 0
        for i in range(iterations):
            # Choosing a random axis - preventing same axis from being chosen 2x in a row
            axis = random.randint(1, 4)
            while previousAxis == axis:
                axis = random.randint(1, 4)
            previousAxis = axis
            if axis == 1:
                x += 0.5 * (0 - x)
                y += 0.5 * (0 - y)
            elif axis == 2:
                x += 0.5 * (1 - x)
                y += 0.5 * (0 - y)
            elif axis == 3:
                x += 0.5 * (1 - x)
                y += 0.5 * (1 - y)
            else:
                x += 0.5 * (0 - x)
                y += 0.5 * (1 - y)
            xVals.append(x)
            yVals.append(y)
    plt.scatter(xVals, yVals, s=1, color='k')
    plt.show()


if __name__ == "__main__":
    main()
