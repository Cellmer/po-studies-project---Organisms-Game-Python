from plant import Plant
from animal import Animal
from tkinter import *
from PIL import ImageTk, Image
import random


class SosnowskyHogweed(Plant):
    def __init__(self, field, world):
        super().__init__(field, 10, world)
        self._name = "Sosnowsky hogweed"

    def draw(self, size, window, x, y):
        img = Image.open("img/sosnowsky_hogweed.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return SosnowskyHogweed(field, world)

    def collision(self, attacker):
        if attacker.defended(self):
            super().collision(attacker)
        elif attacker.has_run_away():
            # jeśli organizm nie jest w stanie ucieczki to wyzeruj pole na którym się znajduje
            if attacker._field.get_organism() == attacker:
                attacker._field.set_organism(0)
            attacker.set_field(self.get_field())
            # print(attacker._name + " has run away from a " + self._name)
            Label(self.get_world().log, text=attacker._name + " has run away from a " + self._name).pack()
            attacker.run()
        else:
            super().collision(attacker)
            # jeśli organizm nie jest w stanie ucieczki to wyzeruj pole na którym się znajduje
            if attacker._field.get_organism() == attacker:
                attacker._field.set_organism(0)
            # print(attacker._name + " dies after eating a " + self._name)
            Label(self.get_world().log, text=attacker._name + " dies after eating a " + self._name).pack()
            attacker.kill()

    def action(self, direction):
        self.kill_all()
        super().action(direction)

    def kill_one(self, attacked):
        if attacked.has_run_away():
            # print(attacked._name + " has run away from a " + self._name)
            Label(self.get_world().log, text=attacked._name + " has run away from a " + self._name).pack()
            attacked.run()
        else:
            if not attacked.defended(self):
                attacked.get_field().set_organism(0)
                # print(attacked._name + " dies in confontation with " + self._name)
                Label(self.get_world().log, text=attacked._name + " dies in confontation with " + self._name).pack()
                attacked.kill()

    def kill_all(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        while len(moves) > 0:
            random_direction = random.choice(moves)
            width = self.get_world().get_width()
            height = self.get_world().get_height()
            x = self._field.get_x() + random_direction[0]
            y = self._field.get_y() + random_direction[1]
            if 0 <= x < width and 0 <= y < height:
                index = self.get_world().get_field_index(x, y)
                if not self.get_world().get_fields()[index].is_empty():
                    if isinstance(self.get_world().get_fields()[index].get_organism(), Animal):
                        self.kill_one(self.get_world().get_fields()[index].get_organism())
            moves.remove(random_direction)
