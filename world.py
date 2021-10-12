from field import Field
from tkinter import *
import random
from human import Human
from wolf import Wolf
from sheep import Sheep
from fox import Fox
from turtle import Turtle
from antelope import Antelope
from grass import Grass
from sonchus import Sonchus
from guarana import Guarana
from belladonna import Belladonna
from sosnowsky_hogweed import SosnowskyHogweed
from cyber_sheep import CyberSheep


class World:
    def __init__(self, width, height):
        # inicjalizacja wymiarów
        self.__width = width
        self.__height = height
        self.__field_size = 50

        self.root = Tk()
        self.root.geometry(str(width * self.__field_size) + "x" + str(height * self.__field_size))
        self.root.title("GRAND WORLD SIMULATOR made by Michał Cellmer")

        # okienko z opisem rund
        self.log = Toplevel()
        self.log.title("LOG")

        # stwórz listę pól i ustaw ich współrzędne
        self.__fields = []
        empty_fields = []
        for i in range(0, height):
            for j in range(0, width):
                self.__fields.append(Field(j, i))
                empty_fields.append(Field(j, i))

        # dodaj organizmy
        self.__organisms = []
        index = random.randint(0, len(empty_fields))
        self.__organisms.append(Human(self.__fields[index], self))
        self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
        self.player = self.__organisms[len(self.__organisms) - 1]
        empty_fields.remove(empty_fields[index])

        instances_number = 3  # liczba instancji każdego organizmu oprócz człowieka

        # wilki
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Wolf(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # owce
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Sheep(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # lisy
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Fox(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # żółwie
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Turtle(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # antylopy
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Antelope(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # cyber owce
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(CyberSheep(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # trawa
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Grass(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # mlecze
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Sonchus(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # guarana
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Guarana(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # wilcze jagody
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(Belladonna(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

        # barszcz Sosnowskiego
        for i in range(instances_number):
            random_field = random.choice(empty_fields)
            index = self.get_field_index(random_field.get_x(), random_field.get_y())
            self.__organisms.append(SosnowskyHogweed(self.__fields[index], self))
            self.__fields[index].set_organism(self.__organisms[len(self.__organisms) - 1])
            empty_fields.remove(random_field)

    def get_field_index(self, x, y):
        return y * self.__width + x

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_fields(self):
        return self.__fields

    def erase_dead(self):
        for org in self.__organisms:
            if org.is_dead():
                self.__organisms.remove(org)

    def add_organism(self, org):
        self.__organisms.append(org)

    def find_empty_field(self, field):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        while len(moves) > 0:
            random_direction = random.choice(moves)
            new_x = field.get_x() + random_direction[0]
            new_y = field.get_y() + random_direction[1]
            if 0 <= new_x < self.__width and 0 <= new_y < self.__height:
                index = self.get_field_index(new_x, new_y)
                if self.__fields[index].is_empty():
                    return self.__fields[index]
                else:
                    moves.remove(random_direction)
            else:
                moves.remove(random_direction)
        return 0

    def draw_world(self):
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                if self.__fields[self.get_field_index(j, i)].is_empty():
                    b = Button(self.root, command=lambda x=j, y=i: self.show_addition_window(self.__fields[self.get_field_index(x, y)]))
                    b.place(x=j * self.__field_size, y=i * self.__field_size,width=self.__field_size, height=self.__field_size)
                else:
                    self.__fields[self.get_field_index(j, i)].organism.draw(self.__field_size, self.root, j, i)

    def make_turn(self, direction):
        # posortuj organizmy po inicjatywie i wieku
        self.__organisms.sort(key=lambda org: org.get_age())
        self.__organisms.sort(key=lambda org: org.get_initiative(), reverse=True)

        for org in self.__organisms:
            if org.is_dead():
                continue
            if org.get_age() < 0:
                org.increment_age()
                continue
            if type(org) == Human:
                org.action(direction)
            else:
                dir = org.choose_direction()
                org.action(dir)

            org.increment_age()

        self.erase_dead()

    def save_game_state(self):
        file = open("game_state.txt", "w")
        file.write(str(self.__width) + "\n")
        file.write(str(self.__height) + "\n")

        for field in self.__fields:
            if field.is_empty():
                file.write("Empty\n")
            else:
                file.write(field.get_organism()._name + "\n")
                file.write(str(field.get_organism().get_strength()) + "\n")

        file.write(str(self.player.is_immortal()) + "\n")
        file.write(str(self.player.get_count_immortality()))
        file.close()

    def load_game(self):
        file = open("game_state.txt", "r")
        width = int(file.readline())
        height = int(file.readline())

        self.__fields.clear()
        for i in range(0, height):
            for j in range(0, width):
                self.__fields.append(Field(j, i))

        self.__organisms.clear()
        for i in range(int(width)*int(height)):
            name = file.readline()
            if name == "Empty\n":
                continue
            else:
                if name == "Human\n":
                    self.__organisms.append(Human(self.__fields[i], self))
                    self.player = self.__organisms[len(self.__organisms) - 1]
                elif name == "Wolf\n":
                    self.__organisms.append(Wolf(self.__fields[i], self))
                elif name == "Sheep\n":
                    self.__organisms.append(Sheep(self.__fields[i], self))
                elif name == "Fox\n":
                    self.__organisms.append(Fox(self.__fields[i], self))
                elif name == "Turtle\n":
                    self.__organisms.append(Turtle(self.__fields[i], self))
                elif name == "Antelope\n":
                    self.__organisms.append(Antelope(self.__fields[i], self))
                elif name == "Grass\n":
                    self.__organisms.append(Grass(self.__fields[i], self))
                elif name == "Sonchus\n":
                    self.__organisms.append(Sonchus(self.__fields[i], self))
                elif name == "Guarana\n":
                    self.__organisms.append(Guarana(self.__fields[i], self))
                elif name == "Belladonna\n":
                    self.__organisms.append(Belladonna(self.__fields[i], self))
                elif name == "Sosnowsky hogweed\n":
                    self.__organisms.append(SosnowskyHogweed(self.__fields[i], self))
                elif name == "Cyber sheep\n":
                    self.__organisms.append(CyberSheep(self.__fields[i], self))

                strength = file.readline()
                self.__organisms[-1].increase_strength(int(strength) - self.__organisms[-1].get_strength())
                self.__fields[i].set_organism(self.__organisms[len(self.__organisms)-1])

        immortality = file.readline()
        if immortality == "True":
            self.player.activate_immortality()
        count_immortality = file.readline()
        self.player.set_count_immortality(int(count_immortality))

        file.close()

    def show_addition_window(self, field):
        window = Toplevel(bg="green")
        window.title("Add new organism")

        animals = LabelFrame(window, bg="green", text="animals")
        animals.grid(row=0, column=0, padx=20, pady=20)
        plants = LabelFrame(window, bg="green", text="plants")
        plants.grid(row=0, column=1, padx=20, pady=20)

        Button(animals, text="Wolf", bg="purple", height=2, width=9, command=lambda: self.add_new_organism("Wolf", field)).pack()
        Button(animals, text="Sheep", bg="purple", height=2, width=9, command=lambda: self.add_new_organism("Sheep", field)).pack()
        Button(animals, text="Fox", bg="purple", height=2, width=9, command=lambda: self.add_new_organism("Fox", field)).pack()
        Button(animals, text="Turtle", bg="purple", height=2, width=9, command=lambda: self.add_new_organism("Turtle", field)).pack()
        Button(animals, text="Antelope", bg="purple", height=2, width=9, command=lambda: self.add_new_organism("Antelope", field)).pack()
        Button(animals, text="Cyber Sheep", bg="purple", height=2, width=9, command=lambda: self.add_new_organism("Cyber sheep", field)).pack()

        Button(plants, text="Grass", bg="purple", height=2, width=17, command=lambda: self.add_new_organism("Grass", field)).pack()
        Button(plants, text="Sonchus", bg="purple", height=2, width=17, command=lambda: self.add_new_organism("Sonchus", field)).pack()
        Button(plants, text="Guarana", bg="purple", height=2, width=17, command=lambda: self.add_new_organism("Guarana", field)).pack()
        Button(plants, text="Belladonna", bg="purple", height=2, width=17, command=lambda: self.add_new_organism("Belladonna", field)).pack()
        Button(plants, text="Sosnowsky's hogweed", bg="purple", height=2, width=17, command=lambda: self.add_new_organism("Sosnowsky hogweed", field)).pack()

    def add_new_organism(self, name, field):
        if name == "Wolf":
            new_org = Wolf(field, self)
        elif name == "Sheep":
            new_org = Sheep(field, self)
        elif name == "Fox":
            new_org = Fox(field, self)
        elif name == "Turtle":
            new_org = Turtle(field, self)
        elif name == "Antelope":
            new_org = Antelope(field, self)
        elif name == "Cyber sheep":
            new_org = CyberSheep(field, self)
        elif name == "Grass":
            new_org = Grass(field, self)
        elif name == "Sonchus":
            new_org = Sonchus(field, self)
        elif name == "Guarana":
            new_org = Guarana(field, self)
        elif name == "Belladonna":
            new_org = Belladonna(field, self)
        elif name == "Sosnowsky hogweed":
            new_org = SosnowskyHogweed(field, self)

        self.add_organism(new_org)
        field.set_organism(new_org)
        self.draw_world()
        self.root.update()
