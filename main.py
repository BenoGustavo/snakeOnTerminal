from board import Board
from snake import Snake
from apple import Apple

gameBoard = Board()
mainSnake = Snake(gameBoard.getBoardSize()[1])
apples = Apple()

gameBoard.setSnakeInstance(mainSnake)
gameBoard.setAppleInstance(apples)

TheGameIsRunning = True

while TheGameIsRunning:
    gameBoard.printBoard()
    mainSnake.updateSnake()
