# Created by: Zack Isingoma
# Created on: 10th Jan 2022.
# to calculate and display the “square”
# power of 2 starting from 0 until this number

import math
user_input = input("Enter a whole number: ")


def main():

    try:
        user_number = int((user_input))

        for x in range(user_number):
            print(math.sqrt(x))
    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
