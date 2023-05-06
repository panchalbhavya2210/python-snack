import math
import random


def mathRand():
    randomNumb = random.randint(0, 50)
    print(randomNumb)

    count = 0

    while (count != 5):
        inputOfUser = input("Enter Your Guessed Number : ")
        type_conv = int(inputOfUser)
        if (type_conv == randomNumb):
            print('You Guessed The Right Now')
            print(randomNumb)
            break
        elif (type_conv < randomNumb):
            print('Oops You Guessed The Wrong Number')
            print("Hint : Go Bigger")
        elif (type_conv > randomNumb):
            print('Oops You Guessed The Wrong Number')
            print("Hint : Go Smaller")

    count += 1


mathRand()
