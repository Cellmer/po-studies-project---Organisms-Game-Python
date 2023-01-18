import random
from abc import ABC, abstractmethod


class Organism(ABC):
    def __init__(self, field, strength, initiative, world):
        self._field = field
        self._strength = strength
        self.__initiative = initiative
        self._world = world
        self.__dead = False
        self._age = 0

    # poruszanie organizmów do zaimplementowania w klasach dziedziczących
    @abstractmethod
    def action(self, direction):
        pass

    # walka lub rozmnażanie
    @abstractmethod
    def collision(self, attacker):
        pass

    def get_field(self):
        return self._field

    def set_field(self, field):
        self._field = field

    def get_strength(self):
        return self._strength

    def get_initiative(self):
        return self.__initiative

    def get_age(self):
        return self._age

    def get_world(self):
        return self._world

    def is_dead(self):
        return self.__dead

    def increment_age(self):
        self._age += 1

    def increase_strength(self, points):
        self._strength += points

    def choose_direction(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        width = self._world.get_width()
        height = self._world.get_height()
        good_move = False
        while not good_move and len(moves) > 0:
            random_move = random.choice(moves)
            new_x = self._field.get_x() + random_move[0]
            new_y = self._field.get_y() + random_move[1]
            if 0 <= new_x < width and 0 <= new_y < height:
                good_move = True
            else:
                moves.remove(random_move)
        return random_move

    def defended(self, attacker):
        return False

    def has_run_away(self):
        return False

    def kill(self):
        self.__dead = True

    def run(self):
        self.action(self.choose_direction())

    def decrement_age(self):
        self._age -= 1
