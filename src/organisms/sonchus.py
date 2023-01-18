from src.organisms.plant import Plant
from tkinter import *
from PIL import ImageTk, Image


class Sonchus(Plant):
    def __init__(self, field, world):
        super().__init__(field, 0, world)
        self._name = "Sonchus"

    def draw(self, size, window, x, y):
        img = Image.open("../img/sonchus.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Sonchus(field, world)

    def action(self, direction):
        for i in range(3):
            super().action(self.choose_direction())