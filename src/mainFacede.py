from pytimedinput import timedInput
from os import system
from time import sleep
from colorama import Fore

from board import Board
from snake import Snake
from apple import Apple
from menu import gameINIT, gameOver
from utils import clearScreenCommand


class initGameFacede:
    def __init__(self) -> None:
        self.gameBoard = Board()
        self.apples = Apple()
        self.mainSnake = Snake(self.gameBoard.getBoardSize()[1], self.apples)
        self.mainSnake.setBoardSize(self.gameBoard.getBoardSize())

        self.gameBoard.setSnakeInstance(self.mainSnake)
        self.apples.setSnakeInstance(self.mainSnake)

        self.isTheGameRunning = True
        self.FPS = 5

        self.SIZE = (
            self.gameBoard.getBoardSize()[0]
            - len(f"★ Score ★ = ({self.apples.getApplesEated()})") / 2
        )
        self.DIVISOR = int(self.SIZE) * " "

        self.cleanTerminal()

        self.DIFFICULT_CHOICE = gameINIT()

        self.cleanTerminal()

    def cleanTerminal(self):
        system(clearScreenCommand)

    def gameOver(self):
        self.cleanTerminal()
        gameOver(self.apples.getApplesEated(), self.DIFFICULT_CHOICE)

    def run(self):
        previousBoard = None
        previousSnake = None
        while self.isTheGameRunning:
            # Clearing the screen
            print("\033[H", end="")

            # Need too much performace
            # system(clearScreenCommand)

            print(
                f"\n\n{self.DIVISOR}★ Score ★ = ({self.apples.getApplesEated()}){self.DIVISOR}"
            )
            self.gameBoard.setApplePosition(self.apples.getApplePosition())

            currentBoard = self.gameBoard.getBoard()
            currentSnake = self.mainSnake.getSnakeBody()

            if previousBoard != currentBoard or previousSnake != currentSnake:
                self.gameBoard.printBoard()
                previousBoard = currentBoard

            keyPressed, _ = timedInput(
                " ", timeout=1 / self.FPS, maxLength=1, allowCharacters="wasdWASD"
            )

            self.mainSnake.moveSnake(keyPressed.lower())

            self.mainSnake.updateSnake()
            FPS = self.mainSnake.appleCollision(self.FPS, self.DIFFICULT_CHOICE)

            if not self.mainSnake.isSnakeAlive():
                self.mainSnake.setSnakeColor(Fore.RED)
                system(clearScreenCommand)

                self.gameBoard.printBoard()

                sleep(2)
                self.isTheGameRunning = False
