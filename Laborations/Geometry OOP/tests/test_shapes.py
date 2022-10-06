from __future__ import annotations
import sys, os
import unittest # for code at bottom of file
from math import pi

# change directory to where this file is
os.chdir(os.path.dirname(__file__))

# path of folder to import from, one level up from current path ("../")
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)

from shapes import *

    # ----- Tests to run -----
class TestCircle(unittest.TestCase): # TestCircle sub-class of TestCase

    # ----- Attributes used later on, to avoid repeating -----
    def setUp(self):
        self.r, self.x, self.y = 2, 3, 4 # TODO go through variety of values to test

    # ----- Default shape for unit testing -----
    def create_circle(self, r_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1) -> Circle:
        """Creates a default circle, for unit testing, 
        
        Created circle uses r, x, y values defined in setUp method, those values are multiplied by input r_mul, x_mul, y_mul values (default 1)"""
        return Circle(self.r * r_mul, self.x * x_mul, self.y * y_mul)

    # ----- Tests -----
    # test creation of shape with expected values:
    def test_create_circle(self):
        """Testing if Circle instance is created with expected values"""
        c = self.create_circle()
        self.assertEqual(c.radius,  self.r)
        self.assertEqual(c.x,   self.x)
        self.assertEqual(c.y,   self.y)

    def test_create_circle_empty(self):
        c = Circle()

    # test creation of shape with invalid parameters:
    def test_create_circle_string(self): # TODO is there a way to do this for more values without manually typing all of them out?
        """Testing if creating Circle with string parameter raises TypeError"""
        self.assertRaises(TypeError, Circle, "1", 1, 1)
        self.assertRaises(TypeError, Circle, 1, "1", 1)
        self.assertRaises(TypeError, Circle, 1, 1, "1")

    def test_create_circle_negative(self):
        """Testing if creating Circle with invalid measurement raises ValueError"""
        self.assertRaises(ValueError, Circle, 0, 1, 1)
        self.assertRaises(ValueError, Circle, -1, 1, 1)

    # test comparisons of area:
    def test_equality_operator(self):
        """Testing equal (==) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_circle(.5, .5, .5)
        c_large = self.create_circle(2, 2, 2)

        self.assertEqual(c_normal, c_normal)
        self.assertNotEqual(c_normal, c_small)
        self.assertNotEqual(c_normal, c_large)

    def test_lesser_than_operator(self):
        """Testing lesser than (<) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_circle(.5, .5, .5)
        c_large = self.create_circle(2, 2, 2)

        self.assertLess(c_normal, c_large)
        self.assertLess(c_small, c_normal)
        self.assertLess(c_small, c_large)

    def test_greater_than_operator(self):
        """Testing greater than (>) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_circle(.5, .5, .5)
        c_large = self.create_circle(2, 2, 2)

        self.assertGreater(c_normal, c_small)
        self.assertGreater(c_large, c_normal)
        self.assertGreater(c_large, c_small)

    def test_lesser_equal_operator(self):
        """Testing lesser or equal (<=) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_circle(.5, .5, .5)
        c_large = self.create_circle(2, 2, 2)

        self.assertLessEqual(c_large, c_large)
        self.assertLessEqual(c_normal, c_large)
        self.assertLessEqual(c_normal, c_normal)
        self.assertLessEqual(c_small, c_large)
        self.assertLessEqual(c_small, c_normal)
        self.assertLessEqual(c_small, c_small)

    def test_greater_equal_operator(self):
        """Testing greater or equal (>=) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_circle(.5, .5, .5)
        c_large = self.create_circle(2, 2, 2)

        self.assertGreaterEqual(c_large, c_large)
        self.assertGreaterEqual(c_large, c_normal)
        self.assertGreaterEqual(c_large, c_small)
        self.assertGreaterEqual(c_normal, c_normal)
        self.assertGreaterEqual(c_normal, c_small)

    # test of other methods:
    def test_is_unit_circle(self):
        """Testing if circle is unit circle (circle with radius 1 centered in origo)"""
        c = self.create_circle()
        c1 = Circle(1, 0, 0)
        c2 = Circle(2, 0, 0)
        c3 = Circle(1, 0, 1)

        self.assertFalse(c.is_unit_circle())
        self.assertTrue(c1.is_unit_circle()) # is unit circle
        self.assertFalse(c2.is_unit_circle())
        self.assertFalse(c3.is_unit_circle())

    def test_calculate_area(self):
        """Testing if area of circle is calculated correctly"""
        c = self.create_circle()
        self.assertEqual(c.calculate_area(), (pi * self.r ** 2))

    def test_calculate_circumference(self):
        """Testing if circumference of circle is calculated correctly"""
        c = self.create_circle()
        self.assertEqual(c.calculate_circumference(), (2 * pi * self.r))

    def test_move_to(self):
        """Testing if translate (x,y) works as expected"""
        c1 = self.create_circle()
        c1.translate(2, 2)
        self.assertEqual((c1.x, c1.y), (self.x + 2, self.y + 2))

        c2 = self.create_circle()
        c2.translate(-2, -2)
        self.assertEqual((c2.x, c2.y), (self.x - 2, self.y - 2))

    def test_contains_point(self):
        """Testing if contains_point correctly checks for circle containing given point"""
        c = self.create_circle()
        self.assertTrue(c.contains_point(self.x, self.y)) # x, y
        # radius distance units from center of circle:
        self.assertTrue(c.contains_point(self.x + self.r, self.y)) # x + r
        self.assertTrue(c.contains_point(self.x, self.y + self.r)) # y + r
        self.assertTrue(c.contains_point(self.x - self.r, self.y)) # x - r
        self.assertTrue(c.contains_point(self.x, self.y - self.r)) # y - r
        # radius + 1 distance units from center of circle:
        self.assertFalse(c.contains_point(self.x + self.r + 1, self.y)) # x + r + 1
        self.assertFalse(c.contains_point(self.x, self.y + self.r + 1)) # y + r + 1
        self.assertFalse(c.contains_point(self.x - self.r - 1, self.y)) # x - r - 1
        self.assertFalse(c.contains_point(self.x, self.y - self.r - 1)) # y - r - 1

# TODO class for Rectangle checks
    # equivalent checks here, including width and height

# TODO class for Sphere checks
    # equivalent checks here, including zpos and volume

# TODO class for Cuboid checks
    # equivalent checks here, including width, height, length, and volume

if __name__ == "__main__": # execute following code if run from this file:
    unittest.main()