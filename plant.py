from organism import Organism
import random
from tkinter import *


class Plant(Organism):

    def __init__(self, field, strength, world):
        super().__init__(field, strength, 0, world)

    # poruszanie
    def action(self, direction):
        # nowe pole na które ruszył się organizm
        new_field_index = self.get_world().get_field_index(self.get_field().get_x() + direction[0], self.get_field().get_y() + direction[1])
        new_field = self.get_world().get_fields()[new_field_index]
        if new_field.is_empty():
            # print(self._name + " on position: (" + str(self.get_field().get_x()) + ", " + str(
            #     self.get_field().get_y()) + ") seeded to position: (" + str(new_field.get_x()) + ", " + str(
            #     new_field.get_y()) + ")")
            Label(self.get_world().log, text=self._name + " on position: (" + str(self.get_field().get_x()) + ", " + str(
                 self.get_field().get_y()) + ") seeded to position: (" + str(new_field.get_x()) + ", " + str(
                 new_field.get_y()) + ")").pack()
            self.seed(new_field)

    # rozsiewanie
    def seed(self, field):
        new_plant = self.create_new(field, self._world)
        field.set_organism(new_plant)
        new_plant.decrement_age()
        self.get_world().add_organism(new_plant)


    # walka lub rozmnażanie
    def collision(self, attacker):
        # jeśli organizm nie jest w stanie ucieczki to wyzeruj pole na którym się znajduje
        if attacker._field.get_organism() == attacker:
            attacker._field.set_organism(0)
        attacker.set_field(self.get_field())
        self.get_field().set_organism(attacker)
        # print(attacker._name + " ate a " + self._name)
        Label(self.get_world().log, text=attacker._name + " ate a " + self._name).pack()
        self.kill()

    def choose_direction(self):
        rand = random.randint(1, 100)
        if rand <= 5:
            return super().choose_direction()
        return (0, 0)