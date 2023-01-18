from src.organisms.animal import Animal
from tkinter import *
from PIL import ImageTk, Image
import random


class Antelope(Animal):
    def __init__(self, field, world):
        super().__init__(field, 4, 4, world)
        self._name = "Antelope"

    def draw(self, size, window, x, y):
        img = Image.open("../img/antelope.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Antelope(field, world)

    def action(self, direction):
        super().action(self.choose_direction())
        super().action(self.choose_direction())

    def has_run_away(self):
        return random.choice([True, False])

    def run(self):
        new_field = self.get_world().find_empty_field(self.get_field())
        if new_field == 0:
            super().action(self.choose_direction())
        else:
            # jeśli organizm nie jest w stanie ucieczki to wyzeruj pole na którym się znajduje
            if self._field.get_organism() == self:
                self._field.set_organism(0)
            new_field.set_organism(self)
            self.set_field(new_field)
