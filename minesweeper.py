import random
# Van Rossum, G. (2020). The Python Library Reference, release 3.8.2. Python Software Foundation.
# https://docs.python.org/3/library/random.html
import os
# source code: https://github.com/python/cpython/tree/3.10/Lib/os.py
# https://docs.python.org/3/library/os.html

def clear():
    os.system('clear')


game = True
board = []
mineBoard = []

# letters are where the first parameter in board would be, numbers are the second one

for i in range(9):
    board.append(["[]"] * 9)


for i in range(9):
    mineBoard.append(["[]"] * 9)
    
def checkWin():
    otherCounter = 0    
        
    for i in range(9):
        for j in range(9):
            try:
                if int(board[i][j]) > -1:
                    otherCounter += 1
            except (IndexError, TypeError, ValueError):
                continue
    if otherCounter == 71:
        showBoard()
        print("You Win!")
        exit()

def showBoard():
    print(" ͟ ͟1͟ ͟ ͟2͟ ͟ ͟3͟ ͟ ͟4͟ ͟ ͟5͟ ͟ ͟6͟ ͟ ͟7͟ ͟ ͟8͟ ͟ ͟9͟ ͟")
    for i in range(9):
        for j in range(9):
            if board[i][j] == "F":
                board[i][j] += " "
            if isinstance(board[i][j], int):
                board[i][j] = str(board[i][j]) + " "
    for i in range(9):
        print(chr(i + 97) + " " +" ".join(board[i]))

def showMineBoard():
    print(" ͟ ͟1͟ ͟ ͟2͟ ͟ ͟3͟ ͟ ͟4͟ ͟ ͟5͟ ͟ ͟6͟ ͟ ͟7͟ ͟ ͟8͟ ͟ ͟9͟ ͟")
    for i in range(9):
        for j in range(9):
            if isinstance(mineBoard[i][j], str):
                mineBoard[i][j] += " "
            if isinstance(mineBoard[i][j], int):
                mineBoard[i][j] = str(mineBoard[i][j]) + " "
    for i in range(9):
        print(chr(i + 97) + " " +" ".join(mineBoard[i]))


def showMine(row, collumn):
    board[row][collumn] = mineBoard[row][collumn]
    if mineBoard[row][collumn] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if row + i < 0 or collumn + j < 0:
                        continue
                    if not board[row + i][collumn + j] == 0 and mineBoard[row + i][collumn + j] == 0:
                        showMine(row + i, collumn + j)
                    if mineBoard[row + i][collumn + j] == 0:
                        board[row + i][collumn + j] = mineBoard[row + i][collumn + j]
                    if mineBoard[row + i][collumn + j] > 0:
                        board[row + i][collumn + j] = mineBoard[row + i][collumn + j]
                except IndexError:
                    continue
                
    
def gameOver():
    showMineBoard()
    print("You Lose")
    exit()
    
def flag(row, collumn):
    board[row][collumn] = "F"


flagsLeft = 10

def guess():
    global flagsLeft
    print("You have", flagsLeft, "flags left")
    guess = input("What coordinate do you guess (letter then number)?")
    guessRow = guess[0]
    guessRow = ord(guessRow) - 97
    guessCollumn = int(guess[1]) - 1
    try:
        if guess[2] == "F":
            flagsLeft -= 1
            flag(guessRow, guessCollumn)
    except IndexError:
        showMine(guessRow, guessCollumn)
        row = guessRow
        collumn = guessCollumn
        if mineBoard[guessRow][guessCollumn] == "X":
            gameOver()
        
    
    
game = True
timer = True


def gameStart():
    global timer
    assignMines()
    if timer:
        firstGuess()
        timer = False
    
    while game:
        clear()
        print("Hello, and welcome to minesweeper!")
        print("There are ten mines placed, each space tells you how many mines are around it")
        print("Guess your coordinate with the letter then number")
        print("""If you want to flag a spot, type "F" after your coordinate""")
        print("Don't choose the mines and clear all of the spaces")
        checkWin()
        showBoard()
        guess()
        
alsoTime = True        
        
def firstGuess():
    global guessRow
    global guessCollumn
    global alsoTime
    if alsoTime:
        alsoTime = False
        guess = input("What coordinate do you guess (letter then number)?")
        guessRow = guess[0]
        guessRow = ord(guessRow) - 97
        guessCollumn = int(guess[1]) - 1
        try:
            if guess[2] == "F":
                flag(guessRow, guessCollumn)
        except:
            pass
    if not mineBoard[guessRow][guessCollumn] == 0:
        gameStart()
    else:
        showMine(guessRow, guessCollumn)
        


def assign(row, collumn):
    value = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if row + i < 0 or collumn + j < 0:
                    continue
                if mineBoard[row + i][collumn + j] == "X":
                    value += 1
            except IndexError:
                continue
            
    mineBoard[row][collumn] = value
    

def assignMines():
    global mineBoard
    mineBoard = []
    for i in range(9):
        mineBoard.append(["[]"] * 9)
    counter = 0
    for i in range(10):
        row = random.randint(0, 8)
        collumn = random.randint(0, 8)
        mineBoard[row][collumn] = "X"
        
    for i in range(9):
        for j in range(9):
            if mineBoard[i][j] == "X":
                counter += 1
    if counter < 10:
        assignMines()
        
    for i in range(9):
        for j in range(9):
            if mineBoard[i][j] == "X":
                continue
            assign(i, j)


def start():
    print("Hello, and welcome to minesweeper!")
    print("There are ten mines placed, each space tells you how many mines are around it")
    print("Guess your coordinate with the letter then number")
    print("""If you want to flag a spot, type "F" after your coordinate""")
    print("Don't choose the mines and clear all of the spaces")
    showBoard()
    gameStart()

try: 
    start()
except (TypeError, ValueError, IndexError):
    print("Why did you mess up?")
    print("Read the instructions")
    print("It's not that hard")
