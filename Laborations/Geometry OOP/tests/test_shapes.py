from __future__ import annotations
import sys, os
import unittest
from math import pi

# change directory to where this file is
os.chdir(os.path.dirname(__file__))

# path of folder to import from, one level up from current path ("../")
path_to_vector_module = os.path.abspath("../")

sys.path.append(path_to_vector_module)

from shapes import Circle, Rectangle, Sphere, Cuboid

# ----- Tests to run -----
class TestCircle(unittest.TestCase): # TestCircle sub-class of TestCase

    # ----- Attribute values -----
    def setUp(self):
        """Specifies values to use in creation of default test circles"""
        self.r, self.x, self.y = 2, 3, 4 # TODO go through variety of values to test

    # ----- Default circle for unit testing -----
    def create_circle(self, r_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1) -> Circle:
        """Creates a default circle, for unit testing, 
        
        Created circle uses r, x, y values defined in setUp method, those values are multiplied by input r_mul, x_mul, y_mul values (default 1)"""
        return Circle(self.r * r_mul, self.x * x_mul, self.y * y_mul)

    # ----- Tests -----
    def test_create_circle(self):
        """Testing if Circle instance is created with expected values"""
        c = self.create_circle()
        self.assertEqual(c.radius,  self.r)
        self.assertEqual(c.x,       self.x)
        self.assertEqual(c.y,       self.y)

    # ----- Testing creating circles with invalid argument values -----
    def test_create_circle_string(self):
        """Testing if creating Circle with string parameter raises TypeError"""
        self.assertRaises(TypeError, Circle, "1", 1, 1)
        self.assertRaises(TypeError, Circle, 1, "1", 1)
        self.assertRaises(TypeError, Circle, 1, 1, "1")

    def test_create_circle_negative(self):
        """Testing if creating Circle with invalid measurement raises ValueError"""
        self.assertRaises(ValueError, Circle, 0, 1, 1)
        self.assertRaises(ValueError, Circle, -1, 1, 1)

    # ----- Testing comparison operators (comparing area) -----
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

    # ----- Testing other methods -----
    def test_is_unit_circle(self):
        """Testing if circle is unit circle (circle with radius 1 centered in origo)"""
        c1 = Circle(1, 0, 0)
        c2 = Circle(2, 0, 0)
        c3 = Circle(1, 0, 1)

        self.assertTrue(c1.is_unit_circle()) # is unit circle
        self.assertFalse(c2.is_unit_circle())
        self.assertFalse(c3.is_unit_circle())

    def test_calculate_area(self):
        """Testing if area of circle is calculated correctly"""
        c = self.create_circle()
        self.assertEqual(c.area, (pi * self.r ** 2))

    def test_calculate_circumference(self):
        """Testing if circumference of circle is calculated correctly"""
        c = self.create_circle()
        self.assertEqual(c.circumference, (2 * pi * self.r))

    def test_translate(self):
        """Testing if translate (x,y) works as expected"""
        c1 = self.create_circle()
        c1.translate(2, 2)
        self.assertEqual((c1.x, c1.y), (self.x + 2, self.y + 2))

        c2 = self.create_circle()
        c2.translate(-2, -2)
        self.assertEqual((c2.x, c2.y), (self.x - 2, self.y - 2))

    def test_contains_point_true(self):
        """Testing if contains_point correctly checks for circle containing given point"""
        c = self.create_circle()
        self.assertTrue(c.contains_point(self.x, self.y)) # x, y
        # radius distance units from center of circle:
        self.assertTrue(c.contains_point(self.x + self.r, self.y)) # x + r
        self.assertTrue(c.contains_point(self.x, self.y + self.r)) # y + r
        self.assertTrue(c.contains_point(self.x - self.r, self.y)) # x - r
        self.assertTrue(c.contains_point(self.x, self.y - self.r)) # y - r

    def test_contains_point_false(self):
        """Testing if contains_point correctly checks for circle containing given point"""
        c = self.create_circle()
        # radius + 1 distance units from center of circle:
        self.assertFalse(c.contains_point(self.x + self.r + 1, self.y)) # x + r + 1
        self.assertFalse(c.contains_point(self.x, self.y + self.r + 1)) # y + r + 1
        self.assertFalse(c.contains_point(self.x - self.r - 1, self.y)) # x - r - 1
        self.assertFalse(c.contains_point(self.x, self.y - self.r - 1)) # y - r - 1

class TestRectangle(unittest.TestCase): # TestRectangle sub-class of TestCase

    # ----- Attribute values -----
    def setUp(self):
        """Specifies values to use in creation of default test rectangles"""
        self.w, self.h, self.x, self.y = 5, 4, -3, -2 # TODO go through variety of values to test

    # ----- Default rectangle for unit testing -----
    def create_rectangle(self, w_mul: (int | float) = 1, h_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1) -> Rectangle:
        """Creates a default rectangle, for unit testing, 
        
        Created rectangle uses r, x, y values defined in setUp method, those values are multiplied by input r_mul, x_mul, y_mul values (default 1)"""
        return Rectangle(self.w * w_mul, self.h * h_mul, self.x * x_mul, self.y * y_mul)

    # ----- Tests -----
    def test_create_rectangle(self):
        """Testing if Rectangle instance is created with expected values"""
        r = self.create_rectangle()
        self.assertEqual(r.width,   self.w)
        self.assertEqual(r.height,  self.h)
        self.assertEqual(r.x,       self.x)
        self.assertEqual(r.y,       self.y)

    # ----- Testing creating circles with invalid argument values -----
    def test_create_rectangle_string(self):
        """Testing if creating Rectangle with string parameter raises TypeError"""
        self.assertRaises(TypeError, Rectangle, "1", 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, "1", 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, "1", 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "1")

    def test_create_rectangle_negative(self):
        """Testing if creating Rectangle with invalid measurement raises ValueError"""
        self.assertRaises(ValueError, Rectangle, 0, 1, 1, 1)
        self.assertRaises(ValueError, Rectangle, -1, 1, 1, 1)

    # ----- Testing comparison operators (comparing area) -----
    def test_equality_operator(self):
        """Testing equal (==) operator on Circles"""
        r_normal = self.create_rectangle()
        r_small = self.create_rectangle(.5, .5, .5, .5)
        r_large = self.create_rectangle(2, 2, 2, 2)

        self.assertEqual(r_normal, r_normal)
        self.assertNotEqual(r_normal, r_small)
        self.assertNotEqual(r_normal, r_large)

    def test_lesser_than_operator(self):
        """Testing lesser than (<) operator on Circles"""
        r_normal = self.create_rectangle()
        r_small = self.create_rectangle(.5, .5, .5, .5)
        r_large = self.create_rectangle(2, 2, 2, 2)

        self.assertLess(r_normal, r_large)
        self.assertLess(r_small, r_normal)
        self.assertLess(r_small, r_large)

    def test_greater_than_operator(self):
        """Testing greater than (>) operator on Circles"""
        r_normal = self.create_rectangle()
        r_small = self.create_rectangle(.5, .5, .5, .5)
        r_large = self.create_rectangle(2, 2, 2, 2)

        self.assertGreater(r_normal, r_small)
        self.assertGreater(r_large, r_normal)
        self.assertGreater(r_large, r_small)

    def test_lesser_equal_operator(self):
        """Testing lesser or equal (<=) operator on Circles"""
        r_normal = self.create_rectangle()
        r_small = self.create_rectangle(.5, .5, .5, .5)
        r_large = self.create_rectangle(2, 2, 2, 2)

        self.assertLessEqual(r_large, r_large)
        self.assertLessEqual(r_normal, r_large)
        self.assertLessEqual(r_normal, r_normal)
        self.assertLessEqual(r_small, r_large)
        self.assertLessEqual(r_small, r_normal)
        self.assertLessEqual(r_small, r_small)

    def test_greater_equal_operator(self):
        """Testing greater or equal (>=) operator on Circles"""
        r_normal = self.create_rectangle()
        r_small = self.create_rectangle(.5, .5, .5, .5)
        r_large = self.create_rectangle(2, 2, 2, 2)

        self.assertGreaterEqual(r_large, r_large)
        self.assertGreaterEqual(r_large, r_normal)
        self.assertGreaterEqual(r_large, r_small)
        self.assertGreaterEqual(r_normal, r_normal)
        self.assertGreaterEqual(r_normal, r_small)

    # ----- Testing other methods -----
    def test_is_square(self):
        """Testing if rectangle is a square (rectangle with all sides equal)"""
        r1 = Rectangle(3, 3, 2, 2)
        r2 = Rectangle(2, 1, 0, 1)
        r3 = Rectangle(1, 3, 1, 1)

        self.assertTrue(r1.is_equilateral()) # is a square
        self.assertFalse(r2.is_equilateral())
        self.assertFalse(r3.is_equilateral())

    def test_calculate_area(self):
        """Testing if area of rectangle is calculated correctly"""
        r = self.create_rectangle()
        self.assertEqual(r.area, (self.w * self.h))

    def test_calculate_perimeter(self):
        """Testing if perimeter of rectangle is calculated correctly"""
        r = self.create_rectangle()
        self.assertEqual(r.perimeter, (self.w * 2 + self.h * 2))

    def test_translate(self):
        """Testing if translate (x,y) works as expected"""
        r1 = self.create_rectangle()
        r1.translate(2, 2)
        self.assertEqual((r1.x, r1.y), (self.x + 2, self.y + 2))

        r2 = self.create_rectangle()
        r2.translate(-2, -2)
        self.assertEqual((r2.x, r2.y), (self.x - 2, self.y - 2))

    def test_contains_point_true(self):
        """Testing if contains_point correctly checks for rectangle containing given point"""
        r = self.create_rectangle()
        # (width or height) / 2 distance units from center of rectangle:
        self.assertTrue(r.contains_point(self.x + self.w / 2, self.y + self.h / 2)) # top right corner
        self.assertTrue(r.contains_point(self.x - self.w / 2, self.y + self.h / 2)) # top left corner
        self.assertTrue(r.contains_point(self.x - self.w / 2, self.y - self.h / 2)) # bottom left corner
        self.assertTrue(r.contains_point(self.x + self.w / 2, self.y - self.h / 2)) # bottom right corner

    def test_contains_point_false(self):
        """Testing if contains_point correctly checks for rectangle not containing given point"""
        r = self.create_rectangle()
        # (width or height) / .9 distance units from center of rectangle (slightly outside):
        self.assertFalse(r.contains_point(self.x + self.w / .9, self.y + self.h / .9)) # top right corner
        self.assertFalse(r.contains_point(self.x - self.w / .9, self.y + self.h / .9)) # top left corner
        self.assertFalse(r.contains_point(self.x - self.w / .9, self.y - self.h / .9)) # bottom left corner
        self.assertFalse(r.contains_point(self.x + self.w / .9, self.y - self.h / .9)) # bottom right corner

class TestCircle(unittest.TestCase): # TestCircle sub-class of TestCase

    # ----- Attribute values -----
    def setUp(self):
        """Specifies values to use in creation of default test spheres"""
        self.r, self.x, self.y, self.z = 2, 3, 4, 5 # TODO go through variety of values to test

    # ----- Default sphere for unit testing -----
    def create_sphere(self, r_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1, z_mul: (int | float) = 1) -> Sphere:
        """Creates a default sphere, for unit testing, 
        
        Created sphere uses r, x, y, z values defined in setUp method, those values are multiplied by input r_mul, x_mul, y_mul, z_mul values (default 1)"""
        return Sphere(self.r * r_mul, self.x * x_mul, self.y * y_mul, self.z * z_mul)

    # ----- Tests -----
    def test_create_sphere(self):
        """Testing if Sphere instance is created with expected values"""
        c = self.create_sphere()
        self.assertEqual(c.radius,  self.r)
        self.assertEqual(c.x,       self.x)
        self.assertEqual(c.y,       self.y)
        self.assertEqual(c.z,       self.z)

    # ----- Testing creating spheres with invalid argument values -----
    def test_create_sphere_string(self):
        """Testing if creating Sphere with string parameter raises TypeError"""
        self.assertRaises(TypeError, Sphere, "1", 1, 1, 1)
        self.assertRaises(TypeError, Sphere, 1, "1", 1, 1)
        self.assertRaises(TypeError, Sphere, 1, 1, "1", 1)
        self.assertRaises(TypeError, Sphere, 1, 1, 1, "1")

    def test_create_sphere_negative(self):
        """Testing if creating Sphere with invalid measurement raises ValueError"""
        self.assertRaises(ValueError, Sphere, 0, 1, 1, 1)
        self.assertRaises(ValueError, Sphere, -1, 1, 1, 1)

    # ----- Testing comparison operators (comparing area) -----
    def test_equality_operator(self):
        """Testing equal (==) operator on spheres"""
        c_normal = self.create_sphere()
        c_small = self.create_sphere(.5, .5, .5, .5)
        c_large = self.create_sphere(2, 2, 2, 2)

        self.assertEqual(c_normal, c_normal)
        self.assertNotEqual(c_normal, c_small)
        self.assertNotEqual(c_normal, c_large)

    def test_lesser_than_operator(self):
        """Testing lesser than (<) operator on spheres"""
        c_normal = self.create_sphere()
        c_small = self.create_sphere(.5, .5, .5, .5)
        c_large = self.create_sphere(2, 2, 2, 2)

        self.assertLess(c_normal, c_large)
        self.assertLess(c_small, c_normal)
        self.assertLess(c_small, c_large)

    def test_greater_than_operator(self):
        """Testing greater than (>) operator on spheres"""
        c_normal = self.create_sphere()
        c_small = self.create_sphere(.5, .5, .5, .5)
        c_large = self.create_sphere(2, 2, 2, 2)

        self.assertGreater(c_normal, c_small)
        self.assertGreater(c_large, c_normal)
        self.assertGreater(c_large, c_small)

    def test_lesser_equal_operator(self):
        """Testing lesser or equal (<=) operator on spheres"""
        c_normal = self.create_sphere()
        c_small = self.create_sphere(.5, .5, .5, .5)
        c_large = self.create_sphere(2, 2, 2, 2)

        self.assertLessEqual(c_large, c_large)
        self.assertLessEqual(c_normal, c_large)
        self.assertLessEqual(c_normal, c_normal)
        self.assertLessEqual(c_small, c_large)
        self.assertLessEqual(c_small, c_normal)
        self.assertLessEqual(c_small, c_small)

    def test_greater_equal_operator(self):
        """Testing greater or equal (>=) operator on spheres"""
        c_normal = self.create_sphere()
        c_small = self.create_sphere(.5, .5, .5, .5)
        c_large = self.create_sphere(2, 2, 2, 2)

        self.assertGreaterEqual(c_large, c_large)
        self.assertGreaterEqual(c_large, c_normal)
        self.assertGreaterEqual(c_large, c_small)
        self.assertGreaterEqual(c_normal, c_normal)
        self.assertGreaterEqual(c_normal, c_small)

    # ----- Testing other methods -----
    def test_is_unit_shape(self):
        """Testing if sphere is "unit sphere" (sphere with radius 1 centered in origo)"""
        c1 = Sphere(1, 0, 0, 0)
        c2 = Sphere(2, 0, 0, 0)
        c3 = Sphere(1, 0, 0, 1)

        self.assertTrue(c1.is_unit_shape()) # is "unit sphere"
        self.assertFalse(c2.is_unit_shape())
        self.assertFalse(c3.is_unit_shape())

    def test_calculate_area(self):
        """Testing if area of sphere is calculated correctly"""
        c = self.create_sphere()
        self.assertEqual(c.area, (4 * pi * self.r ** 2))

    def test_calculate_volume(self):
        """Testing if volume of sphere is calculated correctly"""
        c = self.create_sphere()
        self.assertEqual(c.volume, ((4/3) * pi * self.r**3))

    def test_translate(self):
        """Testing if translate (x,y) works as expected"""
        c1 = self.create_sphere()
        c1.translate(2, 2, 2)
        self.assertEqual((c1.x, c1.y, c1.z), (self.x + 2, self.y + 2, self.z + 2))

        c2 = self.create_sphere()
        c2.translate(-2, -2, -2)
        self.assertEqual((c2.x, c2.y, c2.z), (self.x - 2, self.y - 2, self.z - 2))

    def test_contains_point_true(self):
        """Testing if contains_point correctly checks for sphere containing given point"""
        c = self.create_sphere()
        self.assertTrue(c.contains_point(self.x, self.y, self.z)) # x, y, z
        # radius distance units from center of sphere:
        self.assertTrue(c.contains_point(self.x + self.r, self.y, self.z)) # x + r
        self.assertTrue(c.contains_point(self.x, self.y + self.r, self.z)) # y + r
        self.assertTrue(c.contains_point(self.x, self.y, self.z + self.r)) # z + r

        self.assertTrue(c.contains_point(self.x - self.r, self.y, self.z)) # x - r
        self.assertTrue(c.contains_point(self.x, self.y - self.r, self.z)) # y - r
        self.assertTrue(c.contains_point(self.x, self.y, self.z - self.r)) # z - r

    def test_contains_point_false(self):
        """Testing if contains_point correctly checks for sphere containing given point"""
        c = self.create_sphere()
        # radius + 1 distance units from center of sphere:
        self.assertFalse(c.contains_point(self.x + self.r + 1, self.y, self.z)) # x + r + 1
        self.assertFalse(c.contains_point(self.x, self.y + self.r + 1, self.z)) # y + r + 1
        self.assertFalse(c.contains_point(self.x, self.y, self.z + self.r + 1)) # z + r + 1

        self.assertFalse(c.contains_point(self.x - self.r - 1, self.y, self.z)) # x - r - 1
        self.assertFalse(c.contains_point(self.x, self.y - self.r - 1, self.z)) # y - r - 1
        self.assertFalse(c.contains_point(self.x, self.y, self.z - self.r - 1)) # z - r - 1

class TestCuboid(unittest.TestCase): # TestCuboid sub-class of TestCase

    # ----- Attribute values -----
    def setUp(self):
        """Specifies values to use in creation of default test cuboids"""
        self.w, self.h, self.l, self.x, self.y, self.z = 1, 1, 1, 0, 0, 0

    # ----- Default cuboid for unit testing -----
    def create_cuboid(self, w_mul: (int | float) = 1, h_mul: (int | float) = 1, l_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1, z_mul: (int | float) = 1) -> Cuboid:
        """Creates a default cuboid, for unit testing, 
        
        Created cuboid uses w, h, l, x, y, z values defined in setUp method, those values are multiplied by input w_mul, h_mul, l_mul x_mul, y_mul, z_mul values (default 1)"""
        return Cuboid(self.w * w_mul, self.h * h_mul, self.l * l_mul, self.x * x_mul, self.y * y_mul, self.z * z_mul)

    # ----- Tests -----
    def test_create_cuboid(self):
        """Testing if Cuboid instance is created with expected values"""
        c = self.create_cuboid()
        self.assertEqual(c.width,   self.w)
        self.assertEqual(c.height,  self.h)
        self.assertEqual(c.length,  self.l)
        self.assertEqual(c.x,       self.x)
        self.assertEqual(c.y,       self.y)
        self.assertEqual(c.z,       self.z)

    # ----- Testing creating circles with invalid argument values -----
    def test_create_cuboid_string(self):
        """Testing if creating Cuboid with string parameter raises TypeError"""
        self.assertRaises(TypeError, Cuboid, "1", 1, 1, 1, 1, 1)
        self.assertRaises(TypeError, Cuboid, 1, "1", 1, 1, 1, 1)
        self.assertRaises(TypeError, Cuboid, 1, 1, "1", 1, 1, 1)
        self.assertRaises(TypeError, Cuboid, 1, 1, 1, "1", 1, 1)
        self.assertRaises(TypeError, Cuboid, 1, 1, 1, 1, "1", 1)
        self.assertRaises(TypeError, Cuboid, 1, 1, 1, 1, 1, "1")

    def test_create_cuboid_negative(self):
        """Testing if creating Cuboid with invalid measurement raises ValueError"""
        self.assertRaises(ValueError, Cuboid, 0, 1, 1, 1, 1, 1) # 0
        self.assertRaises(ValueError, Cuboid, 1, 0, 1, 1, 1, 1) # 0
        self.assertRaises(ValueError, Cuboid, 1, 1, 0, 1, 1, 1) # 0

        self.assertRaises(ValueError, Cuboid, -1, 1, 1, 1, 1, 1) # -1
        self.assertRaises(ValueError, Cuboid, 1, -1, 1, 1, 1, 1) # -1
        self.assertRaises(ValueError, Cuboid, 1, 1, -1, 1, 1, 1) # -1

    # ----- Testing comparison operators (comparing area) -----
    def test_equality_operator(self):
        """Testing equal (==) operator on Circles"""
        c_normal = self.create_cuboid()
        c_small = self.create_cuboid(.5, .5, .5, .5, .5, .5)
        c_large = self.create_cuboid(2, 2, 2, 2, 2, 2)

        self.assertEqual(c_normal, c_normal)
        self.assertNotEqual(c_normal, c_small)
        self.assertNotEqual(c_normal, c_large)

    def test_lesser_than_operator(self):
        """Testing lesser than (<) operator on Circles"""
        c_normal = self.create_cuboid()
        c_small = self.create_cuboid(.5, .5, .5, .5, .5, .5)
        c_large = self.create_cuboid(2, 2, 2, 2, 2, 2)

        self.assertLess(c_normal, c_large)
        self.assertLess(c_small, c_normal)
        self.assertLess(c_small, c_large)

    def test_greater_than_operator(self):
        """Testing greater than (>) operator on Circles"""
        c_normal = self.create_cuboid()
        c_small = self.create_cuboid(.5, .5, .5, .5, .5, .5)
        c_large = self.create_cuboid(2, 2, 2, 2, 2, 2)

        self.assertGreater(c_normal, c_small)
        self.assertGreater(c_large, c_normal)
        self.assertGreater(c_large, c_small)

    def test_lesser_equal_operator(self):
        """Testing lesser or equal (<=) operator on Circles"""
        c_normal = self.create_cuboid()
        c_small = self.create_cuboid(.5, .5, .5, .5, .5, .5)
        c_large = self.create_cuboid(2, 2, 2, 2, 2, 2)

        self.assertLessEqual(c_large, c_large)
        self.assertLessEqual(c_normal, c_large)
        self.assertLessEqual(c_normal, c_normal)
        self.assertLessEqual(c_small, c_large)
        self.assertLessEqual(c_small, c_normal)
        self.assertLessEqual(c_small, c_small)

    def test_greater_equal_operator(self):
        """Testing greater or equal (>=) operator on Circles"""
        c_normal = self.create_cuboid()
        c_small = self.create_cuboid(.5, .5, .5, .5, .5, .5)
        c_large = self.create_cuboid(2, 2, 2, 2, 2, 2)

        self.assertGreaterEqual(c_large, c_large)
        self.assertGreaterEqual(c_large, c_normal)
        self.assertGreaterEqual(c_large, c_small)
        self.assertGreaterEqual(c_normal, c_normal)
        self.assertGreaterEqual(c_normal, c_small)

    # ----- Testing other methods -----
    def test_is_cube(self):
        """Testing if cuboid is a cube (cuboid with all sides equal)"""
        c1 = Cuboid(3, 3, 3, 1, 2, -3)
        c2 = Cuboid(2, 1, 1, 1, -1, 1)
        c3 = Cuboid(1, 1, 11, 1, 1, 1)

        self.assertTrue(c1.is_equilateral()) # is a cube
        self.assertFalse(c2.is_equilateral())
        self.assertFalse(c3.is_equilateral())

    def test_calculate_area(self):
        """Testing if area of cuboid is calculated correctly"""
        c = self.create_cuboid()
        self.assertEqual(c.area, (2 * (self.w * self.h + self.h * self.l + self.l * self.w)))

    def test_calculate_volume(self):
        """Testing if volume of cuboid is calculated correctly"""
        c = self.create_cuboid()
        self.assertEqual(c.volume, (self.w * self.h * self.l))

    def test_calculate_perimeter(self):
        """Testing if perimeter of cuboid is calculated correctly"""
        c = self.create_cuboid()
        self.assertEqual(c.perimeter, ((self.w * 4) + (self.h * 4) + (self.l * 4)))

    def test_translate(self):
        """Testing if translate (x,y) works as expected"""
        c1 = self.create_cuboid()
        c1.translate(2, 2, 2)
        self.assertEqual((c1.x, c1.y, c1.z), (self.x + 2, self.y + 2, self.z + 2))

        c2 = self.create_cuboid()
        c2.translate(-2, -2, -2)
        self.assertEqual((c2.x, c2.y, c2.z), (self.x - 2, self.y - 2, self.z - 2))

    def test_contains_point_true(self):
        """Testing if contains_point correctly checks for cuboid containing given point"""
        c = self.create_cuboid()
        # (width or height) / 2 distance units from center of cuboid:
        self.assertTrue(c.contains_point(self.x + self.w / 2, self.y + self.h / 2, self.z + self.l / 2)) # top corner 1
        self.assertTrue(c.contains_point(self.x + self.w / 2, self.y + self.h / 2, self.z - self.l / 2)) # top corner 2
        self.assertTrue(c.contains_point(self.x - self.w / 2, self.y + self.h / 2, self.z + self.l / 2)) # top corner 3
        self.assertTrue(c.contains_point(self.x - self.w / 2, self.y + self.h / 2, self.z - self.l / 2)) # top corner 4
        self.assertTrue(c.contains_point(self.x + self.w / 2, self.y - self.h / 2, self.z + self.l / 2)) # bottom corner 1
        self.assertTrue(c.contains_point(self.x + self.w / 2, self.y - self.h / 2, self.z - self.l / 2)) # bottom corner 2
        self.assertTrue(c.contains_point(self.x - self.w / 2, self.y - self.h / 2, self.z + self.l / 2)) # bottom corner 3
        self.assertTrue(c.contains_point(self.x - self.w / 2, self.y - self.h / 2, self.z - self.l / 2)) # bottom corner 4

    def test_contains_point_false(self):
        """Testing if contains_point correctly checks for cuboid not containing given point"""
        c = self.create_cuboid()
        # (width or height) / .9 distance units from center of cuboid (slightly outside):
        self.assertFalse(c.contains_point(self.x + self.w / .9, self.y + self.h / .9, self.z + self.l / .9)) # top corner 1
        self.assertFalse(c.contains_point(self.x + self.w / .9, self.y + self.h / .9, self.z - self.l / .9)) # top corner 2
        self.assertFalse(c.contains_point(self.x - self.w / .9, self.y + self.h / .9, self.z + self.l / .9)) # top corner 3
        self.assertFalse(c.contains_point(self.x - self.w / .9, self.y + self.h / .9, self.z - self.l / .9)) # top corner 4

        self.assertFalse(c.contains_point(self.x + self.w / .9, self.y - self.h / .9, self.z + self.l / .9)) # bottom corner 1
        self.assertFalse(c.contains_point(self.x + self.w / .9, self.y - self.h / .9, self.z - self.l / .9)) # bottom corner 2
        self.assertFalse(c.contains_point(self.x - self.w / .9, self.y - self.h / .9, self.z + self.l / .9)) # bottom corner 3
        self.assertFalse(c.contains_point(self.x - self.w / .9, self.y - self.h / .9, self.z - self.l / .9)) # bottom corner 4

class TestShapeInteractions(unittest.TestCase):
    # ----- Attribute values -----
    def setUp(self):
        """Specifies values to use in creation of default test cuboids"""
        self.r, self.w, self.h, self.l = 1, 1, 1, 1 # measurements (must be above 0)
        self.x, self.y, self.z = 0, 0, 0 # coordinates

    # ----- Default circle for unit testing -----
    def create_circle(self, r_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1) -> Circle:
        """Creates a default circle, for unit testing, 
        
        Created circle uses r, x, y values defined in setUp method, those values are multiplied by input r_mul, x_mul, y_mul values (default 1)"""
        return Circle(self.r * r_mul, self.x * x_mul, self.y * y_mul)

    # ----- Default rectangle for unit testing -----
    def create_rectangle(self, w_mul: (int | float) = 1, h_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1) -> Rectangle:
        """Creates a default rectangle, for unit testing, 
        
        Created rectangle uses r, x, y values defined in setUp method, those values are multiplied by input r_mul, x_mul, y_mul values (default 1)"""
        return Rectangle(self.w * w_mul, self.h * h_mul, self.x * x_mul, self.y * y_mul)
    
    # ----- Default sphere for unit testing -----
    def create_sphere(self, r_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1, z_mul: (int | float) = 1) -> Sphere:
        """Creates a default sphere, for unit testing, 
        
        Created sphere uses r, x, y, z values defined in setUp method, those values are multiplied by input r_mul, x_mul, y_mul, z_mul values (default 1)"""
        return Sphere(self.r * r_mul, self.x * x_mul, self.y * y_mul, self.z * z_mul)

    # ----- Default cuboid for unit testing -----
    def create_cuboid(self, w_mul: (int | float) = 1, h_mul: (int | float) = 1, l_mul: (int | float) = 1, x_mul: (int | float) = 1, y_mul: (int | float) = 1, z_mul: (int | float) = 1) -> Cuboid:
        """Creates a default cuboid, for unit testing, 
        
        Created cuboid uses w, h, l, x, y, z values defined in setUp method, those values are multiplied by input w_mul, h_mul, l_mul x_mul, y_mul, z_mul values (default 1)"""
        return Cuboid(self.w * w_mul, self.h * h_mul, self.l * l_mul, self.x * x_mul, self.y * y_mul, self.z * z_mul)

    # ----- Tests -----
    def test_equality_operator(self):
        """Testing equality (==) operator between different shape types"""
        circle1 =       self.create_circle()
        rectangle1 =    self.create_rectangle()
        sphere1 =       self.create_sphere()
        cuboid1 =       self.create_cuboid()
        # testing equality between all combination of shape classes
        self.assertFalse(circle1    == rectangle1)
        self.assertFalse(circle1    == sphere1)
        self.assertFalse(circle1    == cuboid1)
        self.assertFalse(rectangle1 == sphere1)
        self.assertFalse(rectangle1 == cuboid1)
        self.assertFalse(sphere1    == cuboid1)

    def test_lesser_than_operator(self):
        """Testing lesser than (<) operator between different shape types"""
        circle1 =       self.create_circle()
        rectangle1 =    self.create_rectangle()
        sphere1 =       self.create_sphere()
        cuboid1 =       self.create_cuboid()
        # testing lesser than between all combination of shape classes
        self.assertFalse(circle1    < rectangle1)
        self.assertTrue(circle1     < sphere1)
        self.assertTrue(circle1     < cuboid1)
        self.assertTrue(rectangle1  < sphere1)
        self.assertTrue(rectangle1  < cuboid1)
        self.assertFalse(sphere1    < cuboid1)

    def test_greater_than_operator(self):
        """Testing greater than (>) operator between different shape types"""
        circle1 =       self.create_circle()
        rectangle1 =    self.create_rectangle()
        sphere1 =       self.create_sphere()
        cuboid1 =       self.create_cuboid()
        # testing greater than between all combination of shape classes
        self.assertTrue(circle1     > rectangle1)
        self.assertFalse(circle1    > sphere1)
        self.assertFalse(circle1    > cuboid1)
        self.assertFalse(rectangle1 > sphere1)
        self.assertFalse(rectangle1 > cuboid1)
        self.assertTrue(sphere1     > cuboid1)

    def test_lesser_equal_operator(self):
        """Testing lesser equal than (<=) operator between different shape types"""
        circle1 =       self.create_circle()
        rectangle1 =    self.create_rectangle()
        sphere1 =       self.create_sphere()
        cuboid1 =       self.create_cuboid()
        # testing lesser equal than between all combination of shape classes
        self.assertFalse(circle1     <= rectangle1)
        self.assertTrue(circle1    <= sphere1)
        self.assertTrue(circle1    <= cuboid1)
        self.assertTrue(rectangle1 <= sphere1)
        self.assertTrue(rectangle1 <= cuboid1)
        self.assertFalse(sphere1     <= cuboid1)

    def test_greater_equal_operator(self):
        """Testing greater equal than (>=) operator between different shape types"""
        circle1 =       self.create_circle()
        rectangle1 =    self.create_rectangle()
        sphere1 =       self.create_sphere()
        cuboid1 =       self.create_cuboid()
        # testing greater equal than between all combination of shape classes
        self.assertTrue(circle1     >= rectangle1)
        self.assertFalse(circle1    >= sphere1)
        self.assertFalse(circle1    >= cuboid1)
        self.assertFalse(rectangle1 >= sphere1)
        self.assertFalse(rectangle1 >= cuboid1)
        self.assertTrue(sphere1     >= cuboid1)

if __name__ == "__main__": # execute following code if run from this file:
    unittest.main()