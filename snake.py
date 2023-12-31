from colorama import Fore, init

init(autoreset=True)


class Snake:
    def __init__(self, boardHeight, appleInstance) -> None:
        self.snakeColor = Fore.GREEN

        self.snakeBody = [
            (5, boardHeight // 2),
            (4, boardHeight // 2),
            (3, boardHeight // 2),
        ]
        self.DIRECTIONS = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
        }
        self.direction = self.DIRECTIONS["up"]

        self.appleInstance = appleInstance

        self.boardSize = None

    def getSnakeColor(self):
        return self.snakeColor

    def setSnakeColor(self, newcolor):
        self.snakeColor = newcolor

    def getSnakeBody(self):
        """Returns a tuple with the coordinates of the snake tuple = (width,height)"""
        return self.snakeBody

    def setBoardSize(self, boardSize: list):
        self.boardSize = boardSize

    def updateSnake(self):
        """Updates the snake body on the board by an given direction"""

        # Creates a new head based on the direction that was given by the user
        newSnakeHead = (
            self.snakeBody[0][0] + self.direction[0],
            self.snakeBody[0][1] + self.direction[1],
        )

        # Inserting the new head in the snakeBody tuple
        self.snakeBody.insert(0, newSnakeHead)

        # Increse the size of the snake or pop the last segment
        if not self.appleInstance.getAppleState():
            # Removes the last segment of the snake
            self.snakeBody.pop(-1)

        # Sets the apple to unEated
        self.appleInstance.setAppleToUneated()

    def appleCollision(self, FPS, difficulty):
        if self.appleInstance.applePosition == self.snakeBody[0]:
            self.appleInstance.setAppleToEated()
            self.appleInstance.updateApplePosition()
            self.appleInstance.setAppleEatedCouter(1)

            match difficulty:
                case "1":  # Easy
                    FPS += 0.5
                case "2":  # Normal
                    FPS += 1
                case "3":  # Hard
                    FPS += 1.5
                case "4":  # XXHARD
                    FPS += 2.0

            return FPS
        return FPS

    def isSnakeAlive(self) -> bool:
        """Checks if the snake is alive"""
        if (
            # Snake touched the board lateral border
            self.snakeBody[0][0] in (0, self.boardSize[0] - 1)
            # Snake touched the board up and down border
            or self.snakeBody[0][1] in (0, self.boardSize[1] - 1)
            # Snake touched one of his parts
            or self.snakeBody[0] in self.snakeBody[1:]
        ):
            return False
        return True

    def moveSnake(self, keyPressed):
        match keyPressed:
            case "w":
                self.direction = self.DIRECTIONS["up"]
            case "a":
                self.direction = self.DIRECTIONS["left"]
            case "s":
                self.direction = self.DIRECTIONS["down"]
            case "d":
                self.direction = self.DIRECTIONS["right"]
