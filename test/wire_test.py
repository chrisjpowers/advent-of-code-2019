import unittest
from unittest.mock import Mock
from advent.wire import Wire, WirePoint, WireVector


class TestWire(unittest.TestCase):
    def test_parse_wire(self):
        w = Wire.parse("R2,U2,L2")
        expected = Wire([
            WireVector(WirePoint(0,0), "R", 2),
            WireVector(WirePoint(2,0), "U", 2),
            WireVector(WirePoint(2,2), "L", 2)
        ])
        self.assertEqual(w, expected)
    
    def test_points(self):
        w = Wire.parse("R2,U2")
        expected = {
            WirePoint(1,0),
            WirePoint(2,0),
            WirePoint(2,1),
            WirePoint(2,2)
        }
        self.assertEqual(w.points(), expected)

    def test_intersection(self):
        w1 = Wire.parse("R2,U2,L2")
        w2 = Wire.parse("D1,R1,U2,R2")
        expected = {
            WirePoint(1,0),
            WirePoint(2,1)
        }
        self.assertEqual(w1 & w2, expected)
        self.assertEqual(w1.closest_intersection(w2).distance, 1)
    
    def test_closest_intersection(self):
        w1 = Wire.parse("R75,D30,R83,U83,L12,D49,R71,U7,L72")
        w2 = Wire.parse("U62,R66,U55,R34,D71,R55,D58,R83")
        self.assertEqual(w1.closest_intersection(w2).distance, 159)
        w1 = Wire.parse("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
        w2 = Wire.parse("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
        self.assertEqual(w1.closest_intersection(w2).distance, 135)


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