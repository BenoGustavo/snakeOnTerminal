class Board:
    def __init__(self) -> None:
        self.BoardSize = [24, 12]  # W,H
        self.BoardBlock = [
            (column, row)  # Result
            for row in range(self.BoardSize[1])  # getting every index in the width
            for column in range(self.BoardSize[0])  # getting every index in the height
        ]

        self.snakeInstance = None
        self.appleInstance = None

    def setSnakeInstance(self, snakeInstance):
        self.snakeInstance = snakeInstance

    def setAppleInstance(self, appleInstance):
        self.appleInstance = appleInstance

    def getBoardSize(self):
        return self.BoardSize

    def printBoard(self):
        for block in self.BoardBlock:
            if block in self.snakeInstance.getSnakeBody():
                print("X", end="")

            elif block == self.appleInstance.getApplePosition():
                print("a", end="")

            elif block[0] in (0, self.BoardSize[0] - 1):
                print("╏", end="")
            else:
                print(" ", end="")

            if block[1] in (0, self.BoardSize[1] - 1):
                print("─", end="")
            else:
                print(" ", end="")

            if block[0] == self.BoardSize[0] - 1:
                print("")
