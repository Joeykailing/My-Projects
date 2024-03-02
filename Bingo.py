####rules####

# state rules

####file#### 
numbers = open("bingo_board_num.txt","r")
num = list(numbers)
num = "".join(num)
num = num.split("\n")

####board#### 
# first column must have numbers between 1-15, second between 16-30, third between 31-45, fourth between 46-60, fifth between 61-75
board = [[num[0], num[5], num[10], num[15], num[20]],
         [num[1], num[6], num[11], num[16], num[21]],
         [num[2], num[7], num[12], num[17], num[22]],
         [num[3], num[8], num[13], num[18], num[23]],
         [num[4], num[9], num[14], num[19], num[24]]]

####printing board####
def print_board():
    print('   * Player 1 Board *')
    print("  B ", "  I ", "  N ", "  G ", "  O ")
    print('------------------------')
    i = 1
    for row in board:
        print("", end=' ')
        for column in row:
            print(f'|{column}|', end=' ')
        print(i)
        i += 1
    print('------------------------')
    print()

####dictionary####
position = {num[0]: [0, 0], num[1]: [1, 0], num[2]: [2, 0], num[3]: [3, 0], num[4]: [4, 0],
            num[5]: [0, 1], num[6]: [1, 1], num[7]: [2, 1], num[8]: [3, 1], num[9]: [4, 1],
            num[10]: [0, 2], num[11]: [1, 2], num[12]: [2, 2], num[13]: [3, 2], num[14]: [4, 2],
            num[15]: [0, 3], num[16]: [1, 3], num[17]: [2, 3], num[18]: [3, 3], num[19]: [4, 3],
            num[20]: [0, 4], num[21]: [1, 4], num[22]: [2, 4], num[23]: [3, 4], num[24]: [4, 4]}

####bingo number####
import random as r

bingo_number_list = []

def random_num():
    not_good_number = True
    global bingo_number
    while not_good_number:
        bingo_number = r.randint(1, 75)
        if bingo_number in bingo_number_list:
            not_good_number = True
        else:
            bingo_number_list.append(bingo_number)
            not_good_number = False
    if len(str(bingo_number)) < 2:
        bingo_number = str(bingo_number)
        testy = bingo_number
        bingo_number = "0" + testy
        print(f'The Bingo number is: {bingo_number}')
    else:
        print(f'The Bingo number is: {bingo_number}')
    
####replacing board with input####
def change_board():
    board[num_position[0]][num_position[1]] = 'xx'

#### ending game ####
def check():
    global game
    game = True
    for i in range(5):
        # horizontal check
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4]:
            game = False
        # vertical check
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i]:
            game = False
        # diagonal check
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]:
            game = False
        if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]:
            game = False

gameNotOver = True
while gameNotOver:
    # Print board
    print_board()

    random_num()
    for k in range(5):
        if str(bingo_number) in board[k]:
            print("Friendly Hint: This number is on your board")

    # Ask the user for input
    user_input = input('Enter an action: "BINGO" to call bingo, "skip" to skip, "cross" to cross off a number: ')
    if user_input == "BINGO":
        # Check if the user actually got bingo
        check()
        if game == False:
            gameNotOver = False
        else:
            print("You don't have BINGO!")
    elif user_input == "skip":
        # Literally nothing
        print("You skipped your turn!")
    elif user_input == "cross":
        # Ask the user for the point
        board_num = input("Enter the point to cross off: ")
        bypass = True
        try:
            num_position = position[board_num]
        except KeyError:
            print("That's not a point!")
            bypass = False
        if bypass:
            # Check if the users input is a valid placement
            if board_num == str(bingo_number):
                # Change the number on the board to an x
                change_board()
            else:
                # Tell the user they didn't input a valid number
                print("That's not a valid point on your board!")
import turtle as t
import random as r

t.write('BINGO!', align='center', font=('Arial',100,'bold'))

def pen(c):
    t.color(c)

def fireworks():
    t.up()
    x = r.randint(-200, 200)
    y = r.randint(-200, 200)
    t.goto(x, y)
    t.down()
    for i in range(40):
        t.forward(100)
        t.right(180)
        t.forward(100)
        t.right(10)

def fireworks2():
    t.up()
    x = r.randint(-350, 350)
    y = r.randint(-350, 350)
    t.goto(x, y)
    t.down()
    for i in range(40):
        t.forward(25)
        t.right(180)
        t.forward(100)
        t.right(10)

colors = ['red', 'orange', 'yellow', 'violet', 'magenta', 'white', 'LawnGreen', 'OrangeRed', 'cyan']
for i in range(5):
    t.speed(0)
    t.bgcolor('blue')
    t.pensize(4)
    c = colors[r.randint(0, 8)]
    pen(c)
    fireworks()
    t.pensize(4)
    c = colors[r.randint(0, 8)]
    pen(c)
    fireworks2()
t.done()
