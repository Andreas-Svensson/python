import numpy as np

class Shape:
    def __init__(self, shape, color: tuple) -> None: # TODO type hinting to np.array?
        self.shape = shape
        self.color = color

    # TODO properties
    
    def rotate_clockwise(self):
        # TODO check validity of move
        self.shape = np.rot90(self.shape, 3) # rotates 90* counter clockwise 3 times

    def rotate_counter_clockwise(self):
        # TODO check validity of move
        self.shape = np.rot90(self.shape)

    # TODO draw method here instead of in game
    
    def __repr__(self):
        return f"Shape({self.shape=}, {self.color=})"

# TODO class Board
    # TODO __init__

    # TODO properties

    # TODO draw board

# for i in I.shape:
#     print(i) # all indices in shape

# print(I.shape[I.shape>0]) # non-empty indices in shape

# x, y = np.where(I.shape == 1) # index of non-empty indices in shape
# print(x, y)