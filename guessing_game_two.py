#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: OCT 2019
# This program is a guessing game

import random
# this function uses a try statement
random_number = (random.randint(0, 8+1))  # a number between 0 and 9


def main():
    # input
    print("")
    user_input_string = input("Please enter a number from (0-9) : ")
    # process & output
    try:
        user_input_integer = int(user_input_string)
        print("")
        print("You entered an integer correctly")
        print("")
        if user_input_integer >= 9:
            print("Number Too High. Enter a Number from (0-9) only.")
        elif user_input_integer == random_number:
            print("Correct Number!! ----->", random_number)

        else:
            print("Sorry Wrong Number, The Correct Number is:", random_number)
            print("")
    finally:
        print("")
        print("Thanks for playing")


if __name__ == "__main__":
    main()
