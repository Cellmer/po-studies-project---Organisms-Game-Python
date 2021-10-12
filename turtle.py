from animal import Animal
from tkinter import *
from PIL import ImageTk, Image
import random


class Turtle(Animal):
    def __init__(self, field, world):
        super().__init__(field, 2, 1, world)
        self._name = "Turtle"

    def draw(self, size, window, x, y):
        img = Image.open("img/turtle.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Turtle(field, world)

    def defended(self, attacker):
        if attacker.get_strength() < 5:
            return True
        return False

    def choose_direction(self):
        rand = random.randint(0, 4)
        if rand <= 2:
            return 0, 0
        else:
            return super(Animal, self).choose_direction()
