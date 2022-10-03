from __future__ import annotations
import sys, os
import unittest # for code at bottom of file

# change directory to where this file is
os.chdir(os.path.dirname(__file__))

# path of folder to import from, one level up from current path ("../")
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)

from shapes import *

# class TestCircle(unittest.TestCase): # TestCircle sub-class of TestCase

#     # ----- Attributes used later on, to avoid repeating -----
#     def setUp(self):
#         self.r, self.x, self.y = 2, 3, 4 # TODO go through variety of values to test

#     # ----- Default shape for unit testing -----
#     def create_circle(self) -> Circle:
#         return Circle(self.r, self.x, self.y)

#     # ----- Example Tests -----
#     def test_create_circle(self):
#         """Testing if Circle instance is created with expected values"""
#         c = self.create_circle()
#         self.assertEqual(c.radius,  self.r)
#         self.assertEqual(c.x_pos,   self.x)
#         self.assertEqual(c.y_pos,   self.y)

    # def test_equal_circle(self):
    #     c1 = self.create_circle()
    #     c2 = Circle(200000, 3, 4) # TODO changes values automatically
    #     self.assertNotEqual(c1.radius, c2.radius)

    # def test_add_circles(self):
    #     c1 = self.create_circle()
    #     c2 = Circle(2, 3, 4) # TODO change values automatically
    #     self.assertEqual(c1 + c2, Circle(self.r + 2, self.x + 3, self.y + 4))

    # ----- Tests to run -----

class TestCircle(unittest.TestCase): # TestCircle sub-class of TestCase

    # ----- Attributes used later on, to avoid repeating -----
    def setUp(self):
        self.r, self.x, self.y = 2, 3, 4 # TODO go through variety of values to test

    # ----- Default shape for unit testing -----
    def create_circle(self) -> Circle:
        """Default Circle for unit testing"""
        return Circle(self.r, self.x, self.y)

    # ----- Tests -----
    # creation of shape with expected values:
    def test_create_circle(self):
        """Testing if Circle instance is created with expected values"""
        c = self.create_circle()
        self.assertEqual(c.radius,  self.r)
        self.assertEqual(c.x_pos,   self.x)
        self.assertEqual(c.y_pos,   self.y)
    
    def test_create_circle_empty(self):
        c = Circle()

    # creation of shape with invalid parameters:
    def test_create_circle_string(self): # TODO is there a way to do this for more values without manually typing all of them out?
        """Testing if creating Circle with string parameter raises TypeError"""
        self.assertRaises(TypeError, Circle, "1", 1, 1)
        self.assertRaises(TypeError, Circle, 1, "1", 1)
        self.assertRaises(TypeError, Circle, 1, 1, "1")
    
    def test_create_circle_negative(self):
        """Testing if creating Circle with invalid measurement raises ValueError"""
        self.assertRaises(ValueError, Circle, 0, 1, 1)
        self.assertRaises(ValueError, Circle, -1, 1, 1)

    # comparisons of radius, xpos, ypos, area, circumference:
    # TODO check equality
    # TODO check lesser than
    # TODO check greater than
    # TODO check lesser or equal
    # TODO check greater or equal

    # methods:
    # TODO check calc_area
    # TODO check calc_circum
    # TODO check translocate
    # TODO check contains_point
    # TODO check is_circle

# TODO class for Rectangle checks
    # equivalent checks here, including width and height

# TODO class for Sphere checks
    # equivalent checks here, including zpos and volume

# TODO class for Cuboid checks
    # equivalent checks here, including width, height, length, and volume

if __name__ == "__main__": # use this as boilerplate code for now, will go through at some other point
    unittest.main()