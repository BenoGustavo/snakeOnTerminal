from pytimedinput import timedInput

# import keyboard #cant import on linux because i need to sudo

from time import sleep

from board import Board
from snake import Snake
from apple import Apple

gameBoard = Board()
apples = Apple()
mainSnake = Snake(gameBoard.getBoardSize()[1], apples)


gameBoard.setSnakeInstance(mainSnake)
apples.setSnakeInstance(mainSnake)

TheGameIsRunning = True
FPS = 5


while TheGameIsRunning:
    # Clearing the screen
    print("\033[H", end="")

    gameBoard.setApplePosition(apples.getApplePosition())
    gameBoard.printBoard()
    sleep(1 / FPS)

    keyPressed, _ = timedInput(
        " ", timeout=1 / FPS, maxLength=1, allowCharacters="wasd"
    )

    # buttonEvent = keyboard.read_event()
    # if buttonEvent.event_type == keyboard.KEY_DOWN:
    # keyPressed = buttonEvent.name

    mainSnake.moveSnake(keyPressed)

    mainSnake.updateSnake()
    mainSnake.appleCollision()
