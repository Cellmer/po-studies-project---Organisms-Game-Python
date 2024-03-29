from src.organisms.plant import Plant
from tkinter import *
from PIL import ImageTk, Image


class Guarana(Plant):
    def __init__(self, field, world):
        super().__init__(field, 0, world)
        self._name = "Guarana"

    def draw(self, size, window, x, y):
        img = Image.open("../img/guarana.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Guarana(field, world)

    def collision(self, attacker):
        super().collision(attacker)
        attacker.increase_strength(3)
        # print(attacker._name + " strength increased to " + str(attacker.get_strength()) + " after eating guarana!")
        Label(self.get_world().log, text=attacker._name + " strength increased to " + str(attacker.get_strength()) + " after eating guarana!").pack()