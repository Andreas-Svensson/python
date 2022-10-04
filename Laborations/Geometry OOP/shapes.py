from __future__ import annotations # for type hinting with classes and |-operators
from math import pi

class Shape: # super class of geometrical shapes
    """Super class of geometrical shapes: Circle, Rectangle, Sphere, Cuboid"""
    def __init__(self,  x_pos: (int | float) = 0, 
                        y_pos: (int | float) = 0) -> None:

        self.x_pos = x_pos # x-coordinate of shape, default 0
        self.y_pos = y_pos # y-coordinate of shape, default 0
    
    # ----- Properties -----
    @property
    def x_pos(self) -> (int | float):
        return self._x_pos
    
    @x_pos.setter
    def x_pos(self, value: (int | float)) -> (int | float):
        self._x_pos = self.check_coordinate(value) # error handling through check_coordinate method

    @property
    def y_pos(self) -> (int | float):
        return self._y_pos
    
    @y_pos.setter
    def y_pos(self, value: (int | float)) -> (int | float):
        self._y_pos = self.check_coordinate(value) # error handling through check_coordinate method

    # ----- Error handling -----
    def check_coordinate(self, value: (int | float)) -> (int | float):
        """Error handling method for all coordinate values"""
        if not isinstance(value, (int, float)): # value is not int or float:
            raise TypeError(f"Coordinate must be a number, not {type(value)}")
        return value # if all checks have been passed

    def check_measurement(self, value: (int | float)) -> (int | float):
        """Error handling method for all measurement values"""
        if not isinstance(value, (int, float)): # value is not int or float:
            raise TypeError(f"Measurement must be a number, not {type(value)}")
        if value <= 0: # value is not greater than 0:
            raise ValueError(f"Value must be over 0, not {value}")
        return value # if all checks have been passed

    # ----- Operator overloading for Shape class -----
    def __eq__(self, other: Shape) -> bool:
        """Override of equal (==) operator for all shapes"""
        if isinstance(other, type(self)): # if same class
            return self.x_pos == other.x_pos # and same x_pos (TODO: later will be area when implemented)
        else:
            return False

    def __lt__(self, other: Shape) -> bool:
        """Override of lesser than (<) operator for all shapes"""
        if isinstance(other, type(self)): # if same class
            return self.x_pos < other.x_pos # and same x_pos (TODO: later will be area when implemented)
        else:
            return False
            
    def __gt__(self, other: Shape) -> bool:
        """Override of greater than (>) operator for all shapes"""
        if isinstance(other, type(self)): # if same class
            return self.x_pos > other.x_pos # and same x_pos (TODO: later will be area when implemented)
        else:
            return False

    def __le__(self, other: Shape) -> bool:
        """Override of lesser or equal (<=) operator for all shapes"""
        if isinstance(other, type(self)): # if same class
            return self.x_pos <= other.x_pos # and same x_pos (TODO: later will be area when implemented)
        else:
            return False

    def __ge__(self, other: Shape) -> bool:
        """Override of greater or equal (>=) operator for all shapes"""
        if isinstance(other, type(self)): # if same class
            return self.x_pos >= other.x_pos # and same x_pos (TODO: later will be area when implemented)
        else:
            return False

    # ----- String representation -----
    def __repr__(self) -> str:
        return f"Shape(x_pos = {self.x_pos}, y_pos = {self.y_pos})"

    def __str__(self) -> str:
        return f"Shape with x: {self.x_pos}, y: {self.y_pos}"

class Circle(Shape): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Circle, sub-class of Shape"""
    def __init__(self,  radius: (int | float) = 1, 
                        x_pos:  (int | float) = 0, 
                        y_pos:  (int | float) = 0) -> None:

        super().__init__(x_pos, y_pos) # x and y coordinates handled in super class
        self.radius = radius # radius of circle, default 1

    # ----- Properties -----
    @property
    def radius(self) -> (int | float):
        return self._radius

    @radius.setter
    def radius(self, value: (int | float)) -> (int | float):
        self._radius = self.check_measurement(value)  # error handling through check_measurement method

    # ----- Methods -----
    def is_unit_circle(self) -> bool:
        """Checks if Circle is a unit circle (circle with radius 1 centered in origo)"""
        if self.radius == 1 and self.x_pos == 0 and self.y_pos == 0:
            return True
        else:
            return False

    def calculate_area(self) -> float:
        """Calculates area of circle"""
        area = pi * self.radius ** 2
        return area

    # TODO calculate_circumference
    def calculate_circumference(self) -> float:
        """Calculates circumference of circle"""
        area = 2 * pi * self.radius
        return area
        
    # TODO move_to
    # TODO contains_point
    # TODO plot

    # ----- String representation -----
    # TODO __repr__
    # TODO __str__

class Rectangle(Shape): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Rectangle, sub-class of Shape"""
    def __init__(self,  width:  (int | float) = 1, 
                        height: (int | float) = 1, 
                        x_pos:  (int | float) = 0, 
                        y_pos:  (int | float) = 0) -> None:

        super().__init__(x_pos, y_pos) # x and y coordinates handled in super class
        self.width = width      # width of rectangle,   default 1
        self.height = height    # height of rectangle,  default 1
        # TODO self.area
        # TODO self.circumference

    # ----- Properties -----
    # TODO @property
    # TODO @width.setter # containing error handling

    # TODO @property
    # TODO @height.setter # containing error handling

    # ----- Methods -----
    # TODO is_square
    # TODO calculate_area
    # TODO calculate_circumference
    # TODO move_to
    # TODO contains_point
    # TODO plot

    # ----- String representation -----
    # TODO __repr__
    # TODO __str__

class Sphere(Shape): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Sphere, sub-class of Shape"""
    def __init__(self,  radius: (int | float) = 1, 
                        x_pos:  (int | float) = 0, 
                        y_pos:  (int | float) = 0, 
                        z_pos:  (int | float) = 0) -> None:

        super().__init__(x_pos, y_pos) # x and y coordinates handled in super class
        self.radius = radius    # radius of sphere,     default 1
        self.z_pos = z_pos      # z-coord of sphere,    default 0
        # TODO self.area
        # TODO self.circumference
        # TODO self.volume

    # ----- Properties -----
    # TODO @property
    # TODO @radius.setter # containing error handling

    # TODO @property
    # TODO @z_pos.setter # containing error handling

    # ----- Methods -----
    # TODO is_unit_sphere
    # TODO calculate_area
    # TODO calculate_circumference
    # TODO calculate volume
    # TODO move_to
    # TODO contains_point
    # TODO plot

    # ----- String representation -----
    # TODO __repr__
    # TODO __str__
    
class Cuboid(Shape): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Cuboid, sub-class of Shape"""
    def __init__(self,  width:  (int | float) = 1, 
                        height: (int | float) = 1, 
                        length: (int | float) = 1, 
                        x_pos:  (int | float) = 0, 
                        y_pos:  (int | float) = 0, 
                        z_pos:  (int | float) = 0) -> None:

        super().__init__(x_pos, y_pos) # x and y coordinates handled in super class
        self.width = width      # width of cuboid,    default 1
        self.height = height    # height of cuboid,   default 1
        self.length = length    # length of cuboid,   default 1
        self.z_pos = z_pos      # z-coord of cuboid,  default 0
        # TODO self.area
        # TODO self.circumference
        # TODO self.volume

    # ----- Properties -----
    # TODO @property
    # TODO @width.setter # containing error handling

    # TODO @property
    # TODO @height.setter # containing error handling

    # TODO @property
    # TODO @length.setter # containing error handling

    # TODO @property
    # TODO @z_pos.setter # containing error handling

    # ----- Methods -----
    # TODO is_cube
    # TODO calculate_area
    # TODO calculate_circumference
    # TODO calculate volume
    # TODO move_to
    # TODO contains_point
    # TODO plot

    # ----- String representation -----
    # TODO __repr__
    # TODO __str__