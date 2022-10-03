import numpy as np

class Shape:
    def __init__(self, shape, color: tuple) -> None:
        self.shape = shape
        self.color = color
    
    def __repr__(self):
        return f"shape({self.shape=}, {self.color=}"

I = Shape(np.array(([0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0])), color = (0, 255, 255)) # I-shape
O = Shape(np.array(([0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0])), color = (255, 255, 0)) # O-shape
T = Shape(np.array(([0, 1, 0], [1, 1, 1], [0, 0, 0])), color = (153, 0, 255)) # T-shape
J = Shape(np.array(([1, 0, 0], [1, 1, 1], [0, 0, 0])), color = (0, 0, 255)) # J-shape
L = Shape(np.array(([0, 0, 1], [1, 1, 1], [0, 0, 0])), color = (255, 170, 0)) # L-shape
S = Shape(np.array(([0, 1, 1], [1, 1, 0], [0, 0, 0])), color = (0, 255, 0)) # S-shape
Z = Shape(np.array(([1, 1, 0], [0, 1, 1], [0, 0, 0])), color = (255, 0, 0)) # Z-shape

# print("I-" + str(I))
# print("O-" + str(O))
# print("T-" + str(T))
# print("J-" + str(J))
# print("L-" + str(L))
# print("S-" + str(S))
# print("Z-" + str(Z))

for i in I.shape:
    print(i) # all indices in shape

print(I.shape[I.shape>0]) # non-empty indices in shape

x, y = np.where(I.shape == 1) # index of non-empty indices in shape
print(x, y)