from src.organisms.plant import Plant
from tkinter import *
from PIL import ImageTk, Image


class Belladonna(Plant):
    def __init__(self, field, world):
        super().__init__(field, 99, world)
        self._name = "Belladonna"

    def draw(self, size, window, x, y):
        img = Image.open("../img/belladonna.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Belladonna(field, world)

    def collision(self, attacker):
        if attacker.has_run_away():
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