from src.organisms.animal import Animal
from tkinter import *
from PIL import ImageTk, Image
from src.organisms.sosnowsky_hogweed import SosnowskyHogweed


class CyberSheep(Animal):
    def __init__(self, field, world):
        super().__init__(field, 4, 4, world)
        self._name = "Cyber sheep"

    def draw(self, size, window, x, y):
        img = Image.open("../img/cyber_sheep.png")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        image = Label(window, image=img)
        image.image = img
        image.place(x=x * size, y=y * size)

    def create_new(self, field, world):
        return CyberSheep(field, world)

    def choose_direction(self):
        target = self.find_sosnowsky()
        if target != 0:
            if target.get_x() < self.get_field().get_x():
                return (-1, 0)
            if target.get_x() > self.get_field().get_x():
                return (1, 0)
            if target.get_y() < self.get_field().get_y():
                return (0, -1)
            return (0, 1)
        else:
            return super().choose_direction()

    def find_sosnowsky(self):
        min_distance = self.get_world().get_width() * self.get_world().get_width()
        found = False
        for field in self.get_world().get_fields():
            if type(field.get_organism()) == SosnowskyHogweed:
                distance = abs(field.get_x() - self.get_field().get_x()) + abs(field.get_y() - self.get_field().get_y())
                if distance < min_distance:
                    min_distance = distance
                    min_field = field
                    found = True
        if found:
            return min_field
        else:
            return 0

    def defended(self, attacker):
        if type(attacker) == SosnowskyHogweed:
            return True
        return False
