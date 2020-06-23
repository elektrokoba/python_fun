import unittest
import main
import fibonacci
import faktor

class TestStringMethods(unittest.TestCase):
    # def test_partition(self):
    #     self.assertEqual(main.canBePartitioned([1,2,7,3,4,5,5,6,7,8,9,9], 3), True)

    # def test_partition2(self):
    #     self.assertEqual(main.mai([1,2,7,3,4,5,5,6,7,8,9,9], 12), False)

    # def test_partition3(self):
    #     self.assertEqual(fibonacci.fibonacci(1), 1)
    
    def test_partition4(self):
        self.assertEqual(fibonacci.fibonacci(1), 0)

    def test_partition5(self):
        self.assertEqual(fibonacci.fibonacci(0), 0)

    def test_fibonacci_normal(self):
        self.assertEqual(fibonacci.fibonacci(10), 34)
    
    def test_fibonacci_negative(self):
        self.assertEqual(fibonacci.fibonacci(-2), None)

    def test_partition6(self):
        self.assertEqual(faktor.factorial(1), 1)

    def test_partition7(self):
        self.assertEqual(faktor.factorial(0), 1)
    
    def test_partition8(self):
        self.assertEqual(faktor.factorial(2), 2)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__fibonacci__':
    unittest.fibonacci()

if __name__ == '__faktor__':
    unittest.faktor()