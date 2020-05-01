# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

import random

com_num = random.randint(100,999)
#print(com_num)


while True:

    gue_num = input("\nEnter your 3 digit guessed number (press q to stop) : ")

    if gue_num.lower() == 'q':
        break

    com_num = str(com_num)

    if com_num == gue_num:
        print("\nPerfect match!")
        break
    elif com_num[0] == gue_num[0] or com_num[1] == gue_num[1] or com_num[2] == gue_num[2]:
        print("\nMatch: You've guessed a correct number in the correct position")
    elif gue_num[0] in com_num or gue_num[1] in com_num or gue_num[2] in com_num:
        print("\nClose: You've guessed a correct number but in the wrong position")
    else:
        print("\nNope: You haven't guess any of the numbers correctly")
