import random

b = {1:1,2:2,3:3,4:4,5:'X',6:6,7:7,8:8,9:9}
l = []

# the function accepts one parameter containing the board's current status and prints it out to the console
def DisplayBoard(): 

    print(f'''
    +-------+-------+-------+
    |       |       |       |
    |   {b[1]}   |   {b[2]}   |   {b[3]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {b[4]}   |   {b[5]}   |   {b[6]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {b[7]}   |   {b[8]}   |   {b[9]}   |
    |       |       |       |
    +-------+-------+-------+
    ''')

# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
def EnterMove():
    global b,l
    while True:
        choice = input(f"Select your box {l} or q (quit): ")
        if choice == 'q':
            keepplaying = False
            break
            
        choice = int(choice)
        if choice in l:
            b[choice] = 'O'
            break

# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
def MakeListOfFreeFields():
    global b,l
    l = [x for x in b.values() if type(x) == int]
    print(l)

# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
def VictoryFor(sign):
    global b,l

    if b[1] == b[2] == b[3] == sign \
    or b[4] == b[5] == b[6] == sign \
    or b[7] == b[8] == b[9] == sign \
    or b[1] == b[4] == b[7] == sign \
    or b[2] == b[5] == b[8] == sign \
    or b[3] == b[6] == b[9] == sign \
    or b[1] == b[5] == b[9] == sign \
    or b[3] == b[5] == b[7] == sign :
        if sign == 'O':
            print("Player wins")
        else:
            print("Computer wins")
        return True
        
    return False

# the function draws the computer's move and updates the board
def DrawMove():
    global b,l
    
    b[random.choice(l)] = 'X'

# game starts here
DisplayBoard()    
while not (VictoryFor('O') or VictoryFor('X')):
    MakeListOfFreeFields()
    #print(l)
    if l == []:
        print("Tie...exiting")
        break
    else:
        EnterMove()
        print("User's Mvove")
        DisplayBoard()
        MakeListOfFreeFields()
        
        DrawMove()
        print("Computer's Mvove")
        DisplayBoard()
