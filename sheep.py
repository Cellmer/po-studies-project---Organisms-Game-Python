from animal import Animal
from tkinter import *
from PIL import ImageTk, Image


class Sheep(Animal):
    def __init__(self, field, world):
        super().__init__(field, 4, 4, world)
        self._name = "Sheep"

    def draw(self, size, window, x, y):
        img = Image.open("img/sheep.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Sheep(field, world)