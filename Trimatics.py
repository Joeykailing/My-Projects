
direction = input('type "intro" for the rules of the game or press enter to start the game: ').lower()
# RULES
if direction == "intro":
    print("This game is called: Trimatics")
    print("It is a -vintage- math game")
    print("(You may want to expand your screen to fit the board)")
    print()
    print("You will be given a board and a random number between 1 and 50")
    print()
    print("Your goal is to find 3 numbers on the board in a row, column or diagonal")
    print("that multiplies the first two numbers then add or minus last number to obtain the random number given")
    print("you can also minus or add the first two numbers then multiply the last number to reach the number given")
    print()
    input("press enter: ")
    print()
    print("For example when the number is: 48")
    ex = [1,2,4,5,2,5,6,8,
          8,3,3,5,9,7,6,
          4,3,8,1,5,9,9,
          6,1,3,4,3,4,6,
          1,8,9,6,6,3,2,
          1,2,3,5,6,9,1,
          3,7,4,1,3,5,6]
    exboard = [[ex[1], ex[2], ex[3], ex[4], ex[5], ex[6], ex[7]],
             [ex[8], ex[9], ex[10], ex[11], ex[12], ex[13], ex[14]],
             [ex[15], ex[16], ex[17], ex[18], ex[19], ex[20], ex[21]],
             [ex[22], ex[23], ex[24], ex[25], ex[26], ex[27], ex[28]],
             [ex[29], ex[30], ex[31], ex[32], ex[33], ex[34], ex[35]],
             [ex[36], ex[37], ex[38], ex[39], ex[40], ex[41], ex[42]],
             [ex[43], ex[44], ex[45], ex[46], ex[47], ex[48], ex[49]]]
    # printing board
    print()
    print()
    for i in range(len(exboard)):
        print("|", end = ' ')
        for j in range(len(exboard[i])):
            if i == 2 and j == 2:
                print(f"[{exboard[i][j]}]", end=' ')
            elif i == 2 and j == 3:
                print(f"[{exboard[i][j]}]", end=' ')
            elif i == 2 and j == 4:
                print(f"[{exboard[i][j]}]", end=' ')
            elif i == 6 and j == 6:
                print(f"[{exboard[i][j]}]", end=' ')
            elif i == 5 and j == 5:
                print(f"[{exboard[i][j]}]", end=' ')
            elif i == 4 and j == 4:
                print(f"[{exboard[i][j]}]", end=' ')
    
            else:   
                print(f"{exboard[i][j]:^3}", end=' ')
        print("|", end = '')
        print()
        print()
    print("518 is a combination that works as (5 + 1) x 8 = 48")
    print("696 is another combination as 6 x 9 - 6 = 48")
    print("You can answer by entering in the numbers in order")
    print("e.g. ans: 696")
    print()
    input("press enter: ")
    print()
    print("(note that some numbers may not have any combinations)")
    print("commands:")
    print('You can enter "possible" to check the number of combinations possible')
    print('You can enter "skip" to a skip random number given')
    print('You can enter "break" or enter something you shouldn\'t to stop the game')
    print("At the end of the game (after 50 numbers) or if the game is stopped the number of combinations you got correct will be shown and numbers you found the combination of will appear")
    input("enter start to start the game: ")

# trimatics game
import random as r
b = []
for i in range(51):
    board_num = r.randint(1, 9)
    b.append(board_num)
board = [[b[1], b[2], b[3], b[4], b[5], b[6], b[7]],
         [b[8], b[9], b[10], b[11], b[12], b[13], b[14]],
         [b[15], b[16], b[17], b[18], b[19], b[20], b[21]],
         [b[22], b[23], b[24], b[25], b[26], b[27], b[28]],
         [b[29], b[30], b[31], b[32], b[33], b[34], b[35]],
         [b[36], b[37], b[38], b[39], b[40], b[41], b[42]],
         [b[43], b[44], b[45], b[46], b[47], b[48], b[49]]]
# checking ans
def check(a,b,c,num):
    # horizontal left to right
    for i in range(7):
        for j in range(5):
            if int(a) == board[i][j] and int(b) == board[i][j+1] and int(c) == board[i][j+2]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    # horizontal right to left
    for i in range(7):
        for j in range(2,7):
            if int(a) == board[i][j] and int(b) == board[i][j-1] and int(c) == board[i][j-2]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    # vertical up to down
    for i in range(5):
        for j in range(7):
            if int(a) == board[i][j] and int(b) == board[i+1][j] and int(c) == board[i+2][j]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    # vertical down to up
    for i in range(2,7):
        for j in range(7):
            if int(a) == board[i][j] and int(b) == board[i-1][j] and int(c) == board[i-2][j]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    # right diagonal up
    for i in range(2,7):
        for j in range(5):
            if int(a) == board[i][j] and int(b) == board[i-1][j+1] and int(c) == board[i-2][j+2]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    # right diagonal down
    for i in range(5):
        for j in range(5):
            if int(a) == board[i][j] and int(b) == board[i+1][j+1] and int(c) == board[i+2][j+2]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    # left diagonal up
    for i in range(2,7):
        for j in range(2,7):
            if int(a) == board[i][j] and int(b) == board[i-1][j-1] and int(c) == board[i-2][j-2]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    # left diagonal down
    for i in range(5):
        for j in range(2,7):
            if int(a) == board[i][j] and int(b) == board[i+1][j-1] and int(c) == board[i+2][j-2]:
                if int(a) * int(b) + int(c) == num:
                    return True
                if int(a) * int(b) - int(c) == num:
                    return True
                if (int(a) + int(b)) * int(c) == num:
                    return True
                if (int(a) - int(b)) * int(c) == num:
                    return True
    return False
# game
correct = 0
num_list = []
num_defeated = []
for i in range(50):
    try:
        # printing board
        print()
        print()
        for i in range(len(board)):
            print("|", end = ' ')
            for j in range(len(board[i])):
                print(f"{board[i][j]:^3}", end=' ')
            print("|", end = '')
            print()
            print()
        # num
        not_good_number = True
        while not_good_number:
            num = r.randint(1, 50)
            if num in num_list:
                not_good_number = True
            else:
                num_list.append(num)
                not_good_number = False
        # input
        print("Number is:", num)
        print()
        ans = input("ans: ")
        # commands
        if ans == "possible":    
            switch = False
            combination_num = 0
            # horizontal left to right
            for i in range(7):
                for j in range(5):
                    question = check(board[i][j],board[i][j+1],board[i][j+2],num)
                    if question:
                        combination_num += 1
                        switch = True
            # horizontal right to left
            for i in range(7):
                for j in range(2,7):
                    question = check(board[i][j],board[i][j-1],board[i][j-2],num)
                    if question:
                        combination_num += 1
                        switch = True
            # vertical up to down
            for i in range(5):
                for j in range(7):
                    question = check(board[i][j],board[i+1][j],board[i+2][j],num)
                    if question:
                        combination_num += 1
                        switch = True
            # vertical down to up
            for i in range(2,7):
                for j in range(7):
                    question = check(board[i][j],board[i-1][j],board[i-2][j],num)
                    if question:
                        combination_num += 1
                        switch = True
            # right diagonal up
            for i in range(2,7):
                for j in range(5):
                    question = check(board[i][j],board[i-1][j+1],board[i-2][j+2],num)
                    if question:
                        combination_num += 1
                        switch = True
            # right diagonal down
            for i in range(5):
                for j in range(5):
                    question = check(board[i][j],board[i+1][j+1],board[i+2][j+2],num)
                    if question:
                        combination_num += 1
                        switch = True
            # left diagonal up
            for i in range(2,7):
                for j in range(2,7):
                    question = check(board[i][j],board[i-1][j-1],board[i-2][j-2],num)
                    if question:
                        combination_num += 1
                        switch = True
            # left diagonal down
            for i in range(5):
                for j in range(2,7):
                    question = check(board[i][j],board[i+1][j-1],board[i+2][j-2],num)
                    if question:
                        combination_num += 1
                        switch = True     
            print()
            if combination_num == 1:
                print("1 combination is possible")
            elif switch == True:
                print(combination_num, "combinations are possible")
            else:
                print("No combinations are possible")
            print()
            ans = input("ans: ")
        if ans == "skip":
            continue
        else:
            verdict = check(ans[0],ans[1],ans[2],num)
            if verdict == True:
                print("Nice!")
                num_defeated.append(num)
                correct += 1
            else:
                while verdict == False:
                    print("Wrong!")
                    print()
                    ans = input("ans again: ")
                    if ans == 'skip':
                        break
                    if ans == "possible":    
                        switch = False
                        combination_num = 0
                        # horizontal left to right
                        for i in range(7):
                            for j in range(5):
                                question = check(board[i][j],board[i][j+1],board[i][j+2],num)
                                if question:
                                    combination_num += 1
                                    switch = True
                        # horizontal right to left
                        for i in range(7):
                            for j in range(2,7):
                                question = check(board[i][j],board[i][j-1],board[i][j-2],num)
                                if question:
                                    combination_num += 1
                                    switch = True
                        # vertical up to down
                        for i in range(5):
                            for j in range(7):
                                question = check(board[i][j],board[i+1][j],board[i+2][j],num)
                                if question:
                                    combination_num += 1
                                    switch = True
                        # vertical down to up
                        for i in range(2,7):
                            for j in range(7):
                                question = check(board[i][j],board[i-1][j],board[i-2][j],num)
                                if question:
                                    combination_num += 1
                                    switch = True
                        # right diagonal up
                        for i in range(2,7):
                            for j in range(5):
                                question = check(board[i][j],board[i-1][j+1],board[i-2][j+2],num)
                                if question:
                                    combination_num += 1
                                    switch = True
                        # right diagonal down
                        for i in range(5):
                            for j in range(5):
                                question = check(board[i][j],board[i+1][j+1],board[i+2][j+2],num)
                                if question:
                                    combination_num += 1
                                    switch = True
                        # left diagonal up
                        for i in range(2,7):
                            for j in range(2,7):
                                question = check(board[i][j],board[i-1][j-1],board[i-2][j-2],num)
                                if question:
                                    combination_num += 1
                                    switch = True
                        # left diagonal down
                        for i in range(5):
                            for j in range(2,7):
                                question = check(board[i][j],board[i+1][j-1],board[i+2][j-2],num)
                                if question:
                                    combination_num += 1
                                    switch = True        
                        print()
                        if combination_num == 1:
                            print("1 combination is possible")
                        elif switch == True:
                            print(combination_num, "combinations are possible")
                        else:
                            print("No combinations are possible")
                        print()
                        ans = input("ans: ")
                        if ans == 'skip':
                            break
                    verdict = check(ans[0],ans[1],ans[2],num)
                    if verdict == True:
                        print("Nice!")
                        num_defeated.append(num)
                        correct += 1   
    except:
        break
print()
print("You have gotten", correct, "correct!")
print("The numbers you defeated are")
try:
    for i in range(len(num_defeated)-1):
        print(num_defeated[i], end=", ")
    print(num_defeated[-1])
except:
    print("none")