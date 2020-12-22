import random


def guess(n):
    number = random.randint(1, n)
    guessing = 0
    while guessing != number:
        guessing = int(input(f'Guess a number between 1 and {n}:'))

        if guessing > number:
            print("number to high.")
        elif guessing < number:
            print("number to low")
    print(f"waouh {number} is a number, congrats")


guess(10)
