class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.organism = 0

    def is_empty(self):
        if self.organism == 0:
            return True
        return False

    def set_organism(self, organism):
        self.organism = organism

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_organism(self):
        return self.organism

