class Survivor:

    def __init__(self, name):
        self._name = name
        self._wounds = 0
        self._is_dead = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def wounds(self):
        return self._wounds

    @wounds.setter
    def wounds(self, new_wounds):
        self._wounds = new_wounds
        if self._wounds >= 2:

            self._is_dead = True
        else:
            self._is_dead = False 

    @property
    def is_dead(self):
        return self._is_dead
