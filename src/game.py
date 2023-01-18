from tkinter import *
from world import World


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("380x400")
        self.root.title("GRAND WORLD SIMULATOR made by Michał Cellmer")
        self.root.configure(background="green")
        # logo
        self.upper_frame = LabelFrame(self.root, padx=40, pady=10, width=800, bg="green")
        self.upper_frame.grid(row=0, column=0, padx=10, pady=10)

        # główne okno menu
        self.main_frame = LabelFrame(self.root, bg="green")
        self.main_frame.grid(row=1, column=0)

        # kierunek w któym będzie poruszał się gracz w danej rundzie (x, y)
        self.direction = (0, 0)

    # tworzy i pokazuje menu
    def view_menu(self):
        logo = Label(self.upper_frame, text="GRAND WORLD SIMULATOR by Michał Cellmer", bg="green")
        logo.pack()

        Button(self.main_frame, text="New Game", padx=10, pady=5, command=self.choose_size).pack(pady=10)
        Button(self.main_frame, text="Load Game", padx=10, pady=5, command=self.load_game_state).pack(pady=10)
        Button(self.main_frame, text="Quit", padx=10, pady=5, command=self.root.quit).pack(pady=10)
        self.root.mainloop()

    # wyczyść okno z widgetów
    def clear_frame(self, frame):
        elements = frame.pack_slaves()
        for widget in elements:
            widget.destroy()

    # pokazuje okno wyboru rozmiaru mapy
    def choose_size(self):
        self.clear_frame(self.main_frame)
        Label(self.main_frame, text="Enter the width of the world: ", bg="green").pack(pady=10)
        entry_width = Entry(self.main_frame, width=50)
        entry_width.pack()
        Label(self.main_frame, text="Enter the height of the world: ", bg="green").pack(pady=10)
        entry_height = Entry(self.main_frame, width=50)
        entry_height.pack()
        Button(self.main_frame, text="Start game", command=lambda: self.start_game(int(entry_width.get()), int(entry_height.get()))).pack(pady=20)

    # ruch użytkownika
    def get_input(self):
        self.world.root.bind("<Key>", self.check_input)

    def check_input(self, event):
        if event.keysym == "Up":
            if self.world.player.get_field().get_y() == 0:
                # print("You can't move up!")
                Label(self.world.log, text="You can't move up!").pack()
            else:
                self.direction = (0, -1)

        if event.keysym == "Down":
            if self.world.player.get_field().get_y() == self.world.get_height()-1:
                # print("You can't move down!")
                Label(self.world.log, text="You can't move down!").pack()
            else:
                self.direction = (0, 1)

        if event.keysym == "Right":
            if self.world.player.get_field().get_x() == self.world.get_width()-1:
                # print("You can't move right!")
                Label(self.world.log, text="You can't move right!").pack()
            else:
                self.direction = (1, 0)

        if event.keysym == "Left":
            if self.world.player.get_field().get_x() == 0:
                # print("You can't move left!")
                Label(self.world.log, text="You can't move left!").pack()
            else:
                self.direction = (-1, 0)

        if event.keysym == "q":
            if not self.world.player.is_immortal() and self.world.player.get_count_immortality() == 0:
                self.world.player.activate_immortality()
                # print("Immortality activated!")
                Label(self.world.log, text="Immortality activated!").pack()
            elif not self.world.player.is_immortal() and self.world.player.get_count_immortality() < 10:
                # print("You can't activate immortality for the next " + str(10-self.world.player.get_count_immortality()) + " rounds!")
                Label(self.world.log, text="You can't activate immortality for the next " + str(10-self.world.player.get_count_immortality()) + " rounds!").pack()
            elif self.world.player.is_immortal():
                # print("Immortality has already been activated!")
                Label(self.world.log, text="Immortality has already been activated!").pack()

        if event.keysym == "s":
            # print("Game saved!")
            Label(self.world.log, text="Game saved!").pack()
            self.world.save_game_state()

    # rozpoczyna symulację
    def start_game(self, width, height):
        if width > 0 and height > 0:
            self.root.destroy()
            self.world = World(width, height)
            self.game_loop()
        else:
            # print("Podaj dobre wymiary!!!")
            Label(self.root, text="Podaj dobre wymiary!!!").grid(row=2, column=0)

    def load_game_state(self):
        try:
            file = open("../game_state.txt", "r")
            self.root.destroy()
            width = int(file.readline())
            height = int(file.readline())
            self.world = World(width, height)
            file.close()
            self.world.load_game()
            self.game_loop()
        except IOError:
            Label(self.main_frame, text="There is no game to load!!! ", bg="green").pack(pady=10)

    def game_loop(self):
        round = 1
        self.world.draw_world()
        self.world.root.update()
        while not self.world.player.is_dead():
            self.get_input()
            if self.direction != (0, 0):
                self.clear_frame(self.world.log)
                Label(self.world.log, text="Runda " + str(round)).pack()
                self.world.make_turn(self.direction)
                self.direction = (0, 0)
                self.world.draw_world()

                # Uaktualnij nieśmiertelność człowieka
                if self.world.player.is_immortal() or (0 < self.world.player.get_count_immortality() < 10):
                    self.world.player.set_count_immortality(self.world.player.get_count_immortality() + 1)
                    if self.world.player.get_count_immortality() == 5:
                        self.world.player.deactivate_immortality()
                    elif self.world.player.get_count_immortality() == 10:
                        self.world.player.set_count_immortality(0)
                round += 1

            self.world.root.update()
        # print(" You loose!")
        Label(self.world.log, text="YOU LOOSE!").pack()
