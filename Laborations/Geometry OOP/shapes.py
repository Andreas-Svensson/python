from __future__ import annotations # for type hinting with classes and |-operators

class Shape: # super class of geometrical shapes
    """Super class of geometrical shapes: Circle, Rectangle, Sphere, Cuboid"""
    def __init__(self,  x_pos: (int | float) = 0, 
                        y_pos: (int | float) = 0) -> None:

        self.x_pos = x_pos # x-coordinate of shape, default 0
        self.y_pos = y_pos # y-coordinate of shape, default 0
    
    # ----- Properties -----
    # TODO @property
    # TODO @x_pos.setter # containing error handling

    # TODO @property
    # TODO @y_pos.setter # containing error handling

    # ----- Error handling -----
    # TODO check_coordinate # error handling method for all coordinates
    # TODO check_measurement # error handling method for all measurements

    # ----- Operator overloading for Shape class -----
    # TODO __eq__
    # TODO __lt__
    # TODO __gt__
    # TODO __le__
    # TODO __ge__

    # ----- String representation -----
    # TODO __repr__
    # TODO __str__

class Circle(Shape): # sub-class inheriting from Shape
    """Class for geometrical shapes of type Circle, sub-class of Shape"""
    def __init__(self,  radius: (int | float) = 1, 
                        x_pos:  (int | float) = 0, 
                        y_pos:  (int | float) = 0) -> None:

        super().__init__(x_pos, y_pos) # x and y coordinates handled in super class
        self.radius = radius # radius of circle, default 1

    # ----- Properties -----
    # TODO @property
    # TODO @radius.setter # containing error handling

    # ----- Methods -----
    # TODO is_unit_circle
    # TODO calculate_area
    # TODO calculate_circumference
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