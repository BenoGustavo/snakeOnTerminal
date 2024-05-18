from pytimedinput import timedInput
from os import system
from time import sleep
from colorama import Fore

from utils import clearScreenCommand
from board import Board
from snake import Snake
from apple import Apple
from menu import gameINIT, gameOver

gameBoard = Board()
apples = Apple()
mainSnake = Snake(gameBoard.getBoardSize()[1], apples)
mainSnake.setBoardSize(gameBoard.getBoardSize())

gameBoard.setSnakeInstance(mainSnake)
apples.setSnakeInstance(mainSnake)

TheGameIsRunning = True
FPS = 5
SIZE = gameBoard.getBoardSize()[0] - len(f"★ Score ★ = ({apples.getApplesEated()})") / 2
DIVISOR = int(SIZE) * " "

system(clearScreenCommand)

DIFFICULT_CHOICE = gameINIT()

system(clearScreenCommand)

previousBoard = None
previousSnake = None
while TheGameIsRunning:
    # Clearing the screen
    print("\033[H", end="")

    # Need too much performace
    # system(clearScreenCommand)

    print(f"\n\n{DIVISOR}★ Score ★ = ({apples.getApplesEated()}){DIVISOR}")
    gameBoard.setApplePosition(apples.getApplePosition())

    currentBoard = gameBoard.getBoard()
    currentSnake = mainSnake.getSnakeBody()

    if previousBoard != currentBoard or previousSnake != currentSnake:
        gameBoard.printBoard()
        previousBoard = currentBoard

    keyPressed, _ = timedInput(
        " ", timeout=1 / FPS, maxLength=1, allowCharacters="wasdWASD"
    )

    mainSnake.moveSnake(keyPressed.lower())

    mainSnake.updateSnake()
    FPS = mainSnake.appleCollision(FPS, DIFFICULT_CHOICE)

    if not mainSnake.isSnakeAlive():
        mainSnake.setSnakeColor(Fore.RED)
        system(clearScreenCommand)

        gameBoard.printBoard()

        sleep(2)
        TheGameIsRunning = False

system(clearScreenCommand)
gameOver(apples.getApplesEated(), DIFFICULT_CHOICE)
