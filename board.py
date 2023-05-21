from const import *

class Board:
    def __init__(self):
        self.squares = []

    def _create(self):
        self.squares =[[0,0,0,0,0,0,0,0] for col in range(COLS)]
        print(self.squares)
    def _add_pieces(self, color):
        pass

b = Board()
b._create()
