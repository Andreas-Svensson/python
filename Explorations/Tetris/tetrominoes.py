import numpy as np

class Shape:
    def __init__(self, shape) -> None:
        self.shape = shape
    
    def __repr__(self):
        return f"shape:\n{self.shape}"

I = Shape(np.array(([0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]))) # I-shape
O = Shape(np.array(([0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]))) # O-shape
T = Shape(np.array(([0, 1, 0], [1, 1, 1], [0, 0, 0]))) # T-shape
J = Shape(np.array(([1, 0, 0], [1, 1, 1], [0, 0, 0]))) # J-shape
L = Shape(np.array(([0, 0, 1], [1, 1, 1], [0, 0, 0]))) # L-shape
S = Shape(np.array(([0, 1, 1], [1, 1, 0], [0, 0, 0]))) # S-shape
Z = Shape(np.array(([1, 1, 0], [0, 1, 1], [0, 0, 0]))) # Z-shape

print("I-" + str(I))
print("O-" + str(O))
print("T-" + str(T))
print("J-" + str(J))
print("L-" + str(L))
print("S-" + str(S))
print("Z-" + str(Z))