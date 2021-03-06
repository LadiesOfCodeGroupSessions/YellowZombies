#rename game to whatever random name aishah comes up with that day
from main.survivor import Survivor
from main.enum import Level
from operator import attrgetter
from main.game_event import GameEvent


class Game:

    def __init__(self):
        self._survivors = []
        self._history = [GameEvent("Started Game")]
        self._level = Level.BLUE
        # self._game_over = False

    @property
    def survivors(self):
        return self._survivors

    @property
    def history(self):
        return self._history

    @property
    def level(self):
        return self._level

    # @property
    # def game_over(self):
        # return self._game_over

# ahhhh think about this
    def game_status(self):
        survivors_alive = list(filter(lambda s: s.is_dead is False, self.survivors))
        if len(survivors_alive) == 0:
            self._history.append(GameEvent("Game Over"))    
            return False
        else:
            return True

    def survivors_remaining(self):
        return len(self.survivors)

    def add_survivor(self, survivor):
        survivors_name = list(filter(lambda s: s.name == survivor.name, self.survivors))
        if len(survivors_name) > 0:
            raise Exception("Name already used")
        self.survivors.append(survivor)
        self._history.append(GameEvent("Survivor Added"))

        # survivors_name = [sur.name for sur in self.survivors]
        # for sur in self.survivors:
        #     if sur.name == survivor.name:
        #         raise Exception("Name already used")
        # self.survivors.append(survivor)

    def survivor_picks_equipment(self, survivor, equipment):
        survivor.pick_equipment(equipment)
        self._history.append(GameEvent("Survivor Picked Up Equipment"))

    def survivor_gets_an_ouch(self, survivor):
        survivor.ouch()

        self._history.append(GameEvent("Survivor Is Wounded"))
        if survivor.is_dead==True:

            self._history.append(GameEvent("Survivor Is Dead"))



    def survivor_kills_zombie(self, survivor):
        survivor.kills_zombie()

        if survivor.experience == 7:
            self._history.append(GameEvent(f"{survivor.name} levelled up to Yellow"))
            # if yellow is the highest level among survivors, change the game level to Yellow
        elif survivor.experience == 19:
            self._history.append(GameEvent(f"{survivor.name} levelled up to Orange"))

        elif survivor.experience == 43:
            self._history.append(GameEvent(f"{survivor.name} levelled up to Red"))
        
        if survivor.level.value > self.level.value:
            self._level = survivor.level
            self._history.append(GameEvent("game levelled up"))
    