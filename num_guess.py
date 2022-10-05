#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/05
# Asks the user to guess a number between 0 and 9
# Displays a message if they guess the correct number
# (which is 8), Displays another message if they do not


def main():

    # title of the program
    print("Guess the Number!")

    # input for the guessed number
    guess = int(input("Guess a number between 0 and 9: "))

    # if statement if the user guesses it correctly
    if guess == 8:
        print("You guessed the number correctly!")

    # if statement if the user does not guess it correctly
    if guess != 8:
        print("You guessed the number incorrectly. Try again!")


if __name__ == "__main__":
    main()
