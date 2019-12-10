import unittest
from advent import Intcode


class TestIntcode(unittest.TestCase):
    def test_stores_memory_and_pointer(self):
        ic = Intcode([1, 2, 3], pointer=4)
        self.assertEqual(ic.pointer, 4)
        self.assertEqual(ic.memory, [1, 2, 3])
    
    def test_simple_addition(self):
        ic     = Intcode([1, 0, 5, 0, 99, 8])
        target = Intcode([9, 0, 5, 0, 99, 8], pointer=8, done=True)
        self.assertEqual(ic.compute(), target)

    def test_simple_multiplication(self):
        ic     = Intcode([2,4,4,5,99,0])
        target = Intcode([2,4,4,5,99,9801], pointer=8, done=True)
        self.assertEqual(ic.compute(), target)

    def test_simple_done(self):
        ic     = Intcode([99, 1, 2, 3])
        target = Intcode([99, 1, 2, 3], pointer=4, done=True)
        self.assertEqual(ic.compute(), target)
    
    def test_compute(self):
        ic     = Intcode([1,1,1,4,99,5,6,0,99])
        target = Intcode([30,1,1,4,2,5,6,0,99], pointer=12, done=True)
        self.assertEqual(ic.compute(), target)
    
    def test_early_stop(self):
        ic     = Intcode([1,9,10,3,2,3,11,0,99,30,40,50])
        target = Intcode([3500,9,10,70,2,3,11,0,99,30,40,50], pointer=12, done=True)
        self.assertEqual(ic.compute(), target)
    
    def test_replace(self):
        ic = Intcode([0, 1, 2, 3, 4, 5])\
            .replace(2, 98)\
            .replace(4, 99)
        target = Intcode([0, 1, 98, 3, 99, 5])
        self.assertEqual(ic, target)