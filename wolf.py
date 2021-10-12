from animal import Animal
from tkinter import *
from PIL import ImageTk, Image


class Wolf(Animal):
    def __init__(self, field, world):
        super().__init__(field, 9, 5, world)
        self._name = "Wolf"

    def draw(self, size, window, x, y):
        img = Image.open("img/wolf.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Wolf(field, world)