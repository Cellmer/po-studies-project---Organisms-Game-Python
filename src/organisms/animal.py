from src.organisms.organism import Organism
from tkinter import *
from abc import abstractmethod

class Animal(Organism):
    # poruszanie
    def action(self, direction):
        if direction == (0, 0):
            #print(self._name + " on position: (" + str(self.get_field().get_x()) + ", " + str(
              #  self.get_field().get_y()) + ") stayed at his place.")
            Label(self.get_world().log, text=self._name + " on position: (" + str(self.get_field().get_x()) + ", " + str(
                self.get_field().get_y()) + ") stayed at his place.").pack()
        else:
            # nowe pole na które ruszył się organizm
            new_field_index = self.get_world().get_field_index(self.get_field().get_x() + direction[0], self.get_field().get_y() + direction[1])
            new_field = self.get_world().get_fields()[new_field_index]

            if new_field.is_empty():
                # print(self._name + " on position: (" + str(self.get_field().get_x()) + ", " + str(
                #     self.get_field().get_y()) + ") moved on position: (" + str(new_field.get_x()) + ", " + str(
                #     new_field.get_y()) + ")")
                Label(self.get_world().log, text=self._name + " on position: (" + str(self.get_field().get_x()) + ", " + str(
                     self.get_field().get_y()) + ") moved on position: (" + str(new_field.get_x()) + ", " + str(
                     new_field.get_y()) + ")").pack()

                # jeśli organizm nie jest w stanie ucieczki to wyzeruj pole na którym się znajduje
                if self._field.get_organism() == self:
                    self._field.set_organism(0)
                new_field.set_organism(self)
                self.set_field(new_field)
            else:
                new_field.get_organism().collision(self)

    # walka lub rozmnażanie
    def collision(self, attacker):
        if type(self) == type(attacker):
            self.procreate(attacker)
        else:
            if self.defended(attacker):
                # print(self._name + " defended himself from a " + attacker._name)
                Label(self.get_world().log, text=self._name + " defended himself from a " + attacker._name).pack()

            # atakujący wygrywa walkę
            elif attacker.get_strength() >= self.get_strength():
                # jeśli organizm nie jest w stanie ucieczki to wyzeruj pole na którym się znajduje
                if attacker.get_field().get_organism() == attacker:
                    attacker.get_field().set_organism(0)
                attacker.set_field(self._field)
                self._field.set_organism(attacker)

                # atakowany uciekł
                if self.has_run_away():
                    # print(self._name + " has run away from a " + attacker._name)
                    Label(self.get_world().log, text=self._name + " has run away from a " + attacker._name).pack()
                    self.run()

                else:
                    # print(attacker._name + " killed a " + self._name)
                    Label(self.get_world().log, text=attacker._name + " killed a " + self._name).pack()
                    self.kill()

            # atakowany wygrywa walkę
            else:
                # jeśli organizm nie jest w stanie ucieczki to wyzeruj pole na którym się znajduje
                if attacker.get_field().get_organism() == attacker:
                    attacker.get_field().set_organism(0)

                # atakujący uciekł
                if attacker.has_run_away():
                    # print(attacker._name + " has run away from a " + self._name)
                    Label(self.get_world().log, text=attacker._name + " has run away from a " + self._name).pack()
                    attacker.run()
                else:
                    # print(self._name + " killed a " + attacker._name)
                    Label(self.get_world().log, text=self._name + " killed a " + attacker._name).pack()
                    attacker.kill()

    # rozmnażanie
    def procreate(self, partner):
        # nowonarodzone dzieci nie mogą mieć dzieci
        if self._age >= 0 and partner._age >= 0:
            new_field = self._world.find_empty_field(self._field)
            if new_field == 0:
                new_field = self._world.find_empty_field(partner._field)
            if new_field != 0:
                new_animal = self.create_new(new_field, self._world)
                new_animal.decrement_age()
                self._world.add_organism(new_animal)
                new_field.set_organism(new_animal)
                # print(self._name + " gave birth to a child!")
                Label(self.get_world().log, text=self._name + " gave birth to a child!").pack()
            else:
                # print(self._name + " tried to gave birth to a child but there was no place for that!")
                Label(self.get_world().log, text=self._name + " tried to gave birth to a child but there was no place for that!").pack()

    # zwraca nową instancję klasy danego organizmu
    @abstractmethod
    def create_new(self, field, world):
        pass
