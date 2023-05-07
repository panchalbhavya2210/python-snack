import random


def wordRandomizer():
    wordArray = ['Teflon', 'Armonian', 'Agam', 'Panchal', 'Bhavya', 'Godzilla']
    chosenByRob = random.choice(wordArray)

    count = 5

    while (count != 0):
        inputOfUser = input('Enter Your Guessed Word : ')

        if (inputOfUser != chosenByRob):
            print('Oof Try Again')
            continue
        else:
            print('Correct')
            break
    count += 1


wordRandomizer()
