import random
from colorama import Fore, Style
import time

attempts = 6
print(Fore.BLUE + "\nGUESS THE NUMBER BETWEEN 1 & 99..!!")
print(f"You have {attempts} attempts only." + Style.RESET_ALL)
no = random.randint(1, 99)

invalid_attempt_flag = False

i = 0
while i <= attempts + 1:
    i = i + 1
    if i <= attempts:
        if i != attempts:
            print(Fore.YELLOW + f"\nAttempt No. {i}")
        else:
            print(Fore.YELLOW + "\nLast Attempt")

        k = input("Enter Your Number Here : ")
        try:
            m = int(k)
        except ValueError:
            if invalid_attempt_flag:
                print('Invalid Input Again! This counts as an attempt.' + Style.RESET_ALL)
            else:
                print('Invalid Input! Please enter a valid integer next time.' + Style.RESET_ALL)
                i = i - 1
            invalid_attempt_flag = True
            continue

        if m == no:
            if i == attempts:
                time.sleep(4)
            else:
                pass

            print(Fore.GREEN + "\nCONGRATULATIONS..!! YOU WON.")

            if i == 1:
                print("You Guessed It Correct In The First Attempt." + Style.RESET_ALL)
            else:
                print(f"You Guessed It Correct In {i} Attempts." + Style.RESET_ALL)
            break

        elif m < no and i != attempts:
            print(Fore.LIGHTGREEN_EX + "Try a larger number." + Style.RESET_ALL)

        elif m > no and i != attempts:
            print(Fore.LIGHTRED_EX + "Try a smaller number." + Style.RESET_ALL)


    else:
        time.sleep(4)
        print(Fore.RED + "\nYOU LOST..!!")
        print(f"The Number is {no}." + Style.RESET_ALL)
        break