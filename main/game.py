#rename game to whatever random name aishah comes up with that day
from main.survivor import Survivor


class Game:

    def __init__(self):
        self._survivors = []

    @property
    def survivors(self):
        return self._survivors

    def survivors_remaining(self):
        return len(self.survivors)

    def add_survivor(self, survivor):
        self.survivors.append(survivor)

