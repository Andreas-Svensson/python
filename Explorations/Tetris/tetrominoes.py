from re import X
import numpy as np
import pygame

class Shape:
    def __init__(self, shape, color: tuple, x, y) -> None: # TODO type hinting to np.array?
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y

    # TODO properties
    
    def rotate_clockwise(self):
        # TODO check validity of move
        self.shape = np.rot90(self.shape, 3) # rotates 90* counter clockwise 3 times

    def rotate_counter_clockwise(self):
        # TODO check validity of move
        self.shape = np.rot90(self.shape)

    # TODO draw method here instead of in game
    def draw(self, scale):
        x_coord, y_coord = np.where(self.shape == 1)
        rectangles = [pygame.Rect(self.x + a * scale, self.y + b * scale, scale, scale) for a, b in zip(x_coord, y_coord)]
        return rectangles

    def draw2(self, scale, board):
        x_coord, y_coord = np.where(self.shape == 1)
        rectangles = [pygame.Rect(self.x + a * scale, self.y + b * scale, scale, scale) for a, b in zip(x_coord, y_coord)]
        for i in rectangles:
            pygame.draw.rect(board, self.color, i)

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

if __name__ == "__main__":
    I = Shape(np.array(([0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0])), color = (0, 255, 255), x = 3 * 35, y = 0)
    I.draw(35)
