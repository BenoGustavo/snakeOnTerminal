class Snake:
    def __init__(self, boardHeight) -> None:
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

    def getSnakeBody(self):
        return self.snakeBody

    def updateSnake(self):
        ...
