from src.organisms.animal import Animal
from tkinter import *
from PIL import ImageTk, Image


class Human(Animal):
    def __init__(self, field, world):
        super().__init__(field, 5, 4, world)
        self._name = "Human"
        self._immortality = False
        self._count_immortality = 0

    def draw(self, size, window, x, y):
        img = Image.open("../img/human.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x*size, y=y*size)

    def create_new(self, field, world):
        return Human(field, world)

    def is_immortal(self):
        return self._immortality

    def activate_immortality(self):
        self._immortality = True

    def deactivate_immortality(self):
        self._immortality = False

    def get_count_immortality(self):
        return self._count_immortality

    def set_count_immortality(self, value):
        self._count_immortality = value

    def has_run_away(self):
        if self.is_immortal():
            return True
        return False
