from __future__ import annotations
import sys, os
import unittest # for code at bottom of file

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
    def create_circle(self) -> Circle:
        """Creates a default circle, for unit testing"""
        return Circle(self.r, self.x, self.y)
    
    def create_small_circle(self) -> Circle:
        """Creates a circle with all parameters smaller than default one, for unit testing"""
        return Circle(self.r / 2, self.x - 2, self.y - 2)
    
    def create_large_circle(self) -> Circle:
        """Creates a circle with all parameters larger than default one, for unit testing"""
        return Circle(self.r +2, self.x + 2, self.y + 2)

    # ----- Tests -----
    # test creation of shape with expected values:
    def test_create_circle(self):
        """Testing if Circle instance is created with expected values"""
        c = self.create_circle()
        self.assertEqual(c.radius,  self.r)
        self.assertEqual(c.x_pos,   self.x)
        self.assertEqual(c.y_pos,   self.y)

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
        c_small = self.create_small_circle()
        c_large = self.create_large_circle()

        self.assertEqual(c_normal, c_normal)
        self.assertNotEqual(c_normal, c_small)
        self.assertNotEqual(c_normal, c_large)

    def test_lesser_than_operator(self):
        """Testing lesser than (<) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_small_circle()
        c_large = self.create_large_circle()

        self.assertLess(c_normal, c_large)
        self.assertLess(c_small, c_normal)
        self.assertLess(c_small, c_large)

    def test_greater_than_operator(self):
        """Testing greater than (>) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_small_circle()
        c_large = self.create_large_circle()

        self.assertGreater(c_normal, c_small)
        self.assertGreater(c_large, c_normal)
        self.assertGreater(c_large, c_small)

    def test_lesser_equal_operator(self):
        """Testing lesser or equal (<=) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_small_circle()
        c_large = self.create_large_circle()

        self.assertLessEqual(c_large, c_large)
        self.assertLessEqual(c_normal, c_large)
        self.assertLessEqual(c_normal, c_normal)
        self.assertLessEqual(c_small, c_large)
        self.assertLessEqual(c_small, c_normal)
        self.assertLessEqual(c_small, c_small)

    def test_greater_equal_operator(self):
        """Testing greater or equal (>=) operator on Circles"""
        c_normal = self.create_circle()
        c_small = self.create_small_circle()
        c_large = self.create_large_circle()

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
    # TODO check calc_area
    # TODO check calc_circum
    # TODO check translocate
    # TODO check contains_point

# TODO class for Rectangle checks
    # equivalent checks here, including width and height

# TODO class for Sphere checks
    # equivalent checks here, including zpos and volume

# TODO class for Cuboid checks
    # equivalent checks here, including width, height, length, and volume

if __name__ == "__main__": # use this as boilerplate code for now, will go through at some other point
    unittest.main()