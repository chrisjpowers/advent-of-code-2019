import unittest
from unittest.mock import Mock
from advent.wire import Wire, WirePoint, WireVector


class TestWire(unittest.TestCase):
    pass


class TestWireVector(unittest.TestCase):
    def test_parse_vector(self):
        p = WirePoint(3, 2)
        v = WireVector.parse(p, "R75")
        self.assertEqual(v.point, p)
        self.assertEqual(v.direction, "R")
        self.assertEqual(len(v), 75)
    
    def test_vector_points_up(self):
        p = WirePoint(0, 0)
        v = WireVector.parse(p, "U2")
        points = [
            WirePoint(0, 0),
            WirePoint(0, 1),
            WirePoint(0, 2),
        ]
        self.assertEqual(v.points, points)

    def test_vector_points_right(self):
        p = WirePoint(0, 0)
        v = WireVector.parse(p, "R2")
        points = [
            WirePoint(0, 0),
            WirePoint(1, 0),
            WirePoint(2, 0),
        ]
        self.assertEqual(v.points, points)

    def test_vector_points_down(self):
        p = WirePoint(0, 0)
        v = WireVector.parse(p, "D2")
        points = [
            WirePoint(0, 0),
            WirePoint(0, -1),
            WirePoint(0, -2),
        ]
        self.assertEqual(v.points, points)

    def test_vector_points_left(self):
        p = WirePoint(0, 0)
        v = WireVector.parse(p, "L2")
        points = [
            WirePoint(0, 0),
            WirePoint(-1, 0),
            WirePoint(-2, 0),
        ]
        self.assertEqual(v.points, points)
    
    def test_final_point(self):
        p = WirePoint(0, 0)
        v = WireVector.parse(p, "R2")
        expected = WirePoint(2, 0)
        self.assertEqual(v.final_point, expected)
    
    def test_intersection(self):
        v1 = WireVector(WirePoint(0, 2), "R", 5)
        v2 = WireVector(WirePoint(2, 0), "U", 5)
        self.assertEqual(v1 & v2, {WirePoint(2, 2)})


class TestWirePoint(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(WirePoint(5, 5).distance, 10)
        self.assertEqual(WirePoint(5, -3).distance, 8)
        self.assertEqual(WirePoint(-5, -3).distance, 8)
    
    def test_eq(self):
        self.assertEqual(WirePoint(5,5), WirePoint(5,5))