from random import randint


class Apple:
    def __init__(self) -> None:
        self.applePosition = (randint(1, 22), randint(1, 22))
        self.isAppleEated = False
        self.appleEatedCouter = 0

        self.snakeInstance = None

    def setSnakeInstance(self, snakeInstance):
        self.snakeInstance = snakeInstance

    def getApplesEated(self) -> int:
        return self.appleEatedCouter

    def setAppleEatedCouter(self, value: int):
        self.appleEatedCouter += value

    def getApplePosition(self):
        return self.applePosition

    def setAppleToEated(self):
        self.isAppleEated = True

    def setAppleToUneated(self):
        self.isAppleEated = False

    def getAppleState(self):
        return self.isAppleEated

    def updateApplePosition(self):
        self.applePosition = (randint(1, 22), randint(1, 22))
        while self.applePosition in self.snakeInstance.getSnakeBody():
            self.applePosition = (randint(1, 22), randint(1, 22))
        return
