from random import randint
print("\n"*32)
board = [" "," "," "," "," "," "," "," "," "]
validChoices = ["1","2","3","4","5","6","7","8","9"]
winStates = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
symbol = ("X","O")
isTie = True

# starts the game
def gameStart():
    print("\n"+"~"*25)
    print("G A M E         S T A R T")
    print("~"*25)
    print("Do you want to make the first move?")
    valid = False
    validPicks = {"Y","y","N","n"}
    while(valid == False):
        choice = input("Y/N : ")
        if (choice in validPicks):
            valid = True
        else:
            print("Invalid input. Try again.")
    if (choice.lower() == "y"):
        return 0
    else:
        return 1

# choosing your opponent
def chooseEnemy():
    print("Which enemy do you want to fight?")
    print("0 = Stupid enemy")
    # print("1 = Normal enemy")
    # print("2 = Smart enemy")
    valid = False
    validDiffs = {"0","1","2"}
    while(valid == False):
        choice = input("0/1/2 : ")
        if (choice in validDiffs):
            return int(choice)
        else:
            print("Invalid input. Try again.")

# draws the board
def drawBoard(board):
    print("\n"*32)
    drawHoriz = "+"+"---------+"*3
    for i in range(0,19):
        str_ = "|"
        x1 = 3*(i//6)
        if (i%6==0):
            print(drawHoriz)
            continue
        elif (i%6==1 or i%6==5):
            for j in range(0,3):
                x2 = x1 + j
                if (board[x2]==" "):
                    str_ += "         |"
                elif (board[x2]=="X"):
                    str_ += " XX   XX |"
                else:
                    str_ += "  OOOOO  |"
        elif (i%6==2 or i%6==4):
            for j in range(0,3):
                x2 = x1 + j
                if (board[x2]==" "):
                    str_ += "         |"
                elif (board[x2]=="X"):
                    str_ += "  XX XX  |"
                else:
                    str_ += " OO   OO |"
        else:
            for j in range(0,3):
                x2 = x1 + j
                if (board[x2]==" "):
                    str_ += "    "+str(x2+1)+"    |"
                elif (board[x2]=="X"):
                    str_ += "   XXX   |"
                else:
                    str_ += " OO   OO |"
        print(str_)
    print("\n")

# player's move
def playerMove(playerId,validChoices):
    if(playerId == 0):
        print("X"*17)
        print("XX  Your move  XX")
        print("X"*17)
    else:
        print("O"*17)
        print("OO  Your move  OO")
        print("O"*17)
    valid = False
    while(valid == False):
        choice = input("Pick a square : ")
        if (choice in validChoices):
            valid = True
        else:
            print("Invalid input. Try again.")
    return choice

# stupid enemy
def stupidMove(validChoices):
    selection = randint(0,len(validChoices)-1)
    return validChoices[selection]

# check if someone has won
def checkForWin(board,winStates):
    for i in range(0,8):
        set_ = {board[winStates[i][0]],board[winStates[i][1]],board[winStates[i][2]]}
        if (len(set_)==1 and (" " not in set_)):
            return True
    return False

# normal enemy
def normalMove(board,validChoices):
    print("hello world")
    for i in range(0,len(validChoices)-1):
        print("hello world")

# smart enemy
def smartMove(board,validChoices):
    print("hello world")

# main game code
playerId = gameStart()
difficulty = chooseEnemy()
drawBoard(board)
for step in range(0,9):
    if (step%2 == playerId):
        chosen = playerMove(playerId,validChoices)
        board[int(chosen)-1] = symbol[playerId]
    else:
        if (difficulty == 0):
            chosen = stupidMove(validChoices)
        elif (difficulty == 1):
            chosen = normalMove(validChoices)
        else:
            chosen = smartMove(validChoices)
        board[int(chosen)-1] = symbol[1-playerId]
    validChoices.remove(chosen)
    drawBoard(board)
    if (checkForWin(board,winStates) == True):
        isTie = False
        if (step%2 == playerId):
            drawBoard(board)
            print("You have won the game!")
        else:
            drawBoard(board)
            print("You have lost the game.")
        break
if (isTie == True):
    drawBoard(board)
    print("The game has ended in a tie.")