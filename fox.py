from animal import Animal
from tkinter import *
from PIL import ImageTk, Image
import random


class Fox(Animal):
    def __init__(self, field, world):
        super().__init__(field, 3, 7, world)
        self._name = "Fox"

    def draw(self, size, window, x, y):
        img = Image.open("img/fox.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return Fox(field, world)

    def choose_direction(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        width = self._world.get_width()
        height = self._world.get_height()
        while len(moves) > 0:
            random_move = random.choice(moves)
            new_x = self._field.get_x() + random_move[0]
            new_y = self._field.get_y() + random_move[1]
            if 0 <= new_x < width and 0 <= new_y < height:
                new_field_index = self._world.get_field_index(new_x, new_y)
                new_field = self._world.get_fields()[new_field_index]
                if new_field.is_empty() or new_field.get_organism().get_strength() <= self._strength:
                    return random_move
                else:
                    moves.remove(random_move)

            else:
                moves.remove(random_move)
        return (0, 0)