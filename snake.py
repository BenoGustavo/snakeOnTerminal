class Snake:
    def __init__(self, boardHeight, appleInstance) -> None:
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

    def getSnakeBody(self):
        """Returns a tuple with the coordinates of the snake tuple = (width,height)"""
        return self.snakeBody

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

    def appleCollision(self):
        if self.appleInstance.applePosition == self.snakeBody[0]:
            self.appleInstance.setAppleToEated()
            self.appleInstance.updateApplePosition()
            self.appleInstance.setAppleEatedCouter(1)

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
