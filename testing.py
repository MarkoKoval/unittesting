import algorithms
import unittest

class TestAlgorithms(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(algorithms.quick_sort([8, 4, 4, 5]),[ 4, 4, 5,8])
    def test_binary_search(self):
        self.assertEqual(algorithms.binary_search([ 4, 4, 5,8], 8),3)
        self.assertRaises(algorithms.UnsortedException, algorithms.binary_search, [4, 1, 5, 8], 8)
    def test_points_to_polynomial(self):
        self.assertEqual(algorithms.points_to_polynomial([[1, 5], [2, 2]]),"f(x)=x^1*-3.0+x^0*8.0")
        self.assertRaises(algorithms.EmptyCoordinatesException, algorithms.points_to_polynomial, [])
    def test_linear_search(self):
        self.assertEqual(algorithms.linear_search([8, 4, 4, 5],4),1)
        self.assertIsNone(algorithms.linear_search([8, 4, 4, 5],99))
    def test_determinant(self):
        self.assertEqual(algorithms.determinant([[1, 5, 1], [8, 4,3],[5,9,5] ]), -80)

    def test_string_reverse(self):
        self.assertEqual(algorithms.string_reverse("marko"),"okram")
        self.assertIsNone(algorithms.string_reverse( 127))
    def test_is_palindrome(self):
        self.assertEqual(algorithms.is_palindrome("ABBA"), True)
    def test_naivePatternSearch(self):
        self.assertEqual(algorithms.naivePatternSearch("hello world world", "world"),[6,12])
        self.assertIsNone(algorithms.naivePatternSearch( ["hello world world", "hello world world" ], "world"))
    def test_euclid(self):
        self.assertEqual( algorithms.euclid(6,3),3)
        self.assertLessEqual(algorithms.euclid(12,6),7)
    def test_checkTriangleValidity(self):
        self.assertEqual(algorithms.checkTriangleValidity(5,10,7),True)
        self.assertFalse(algorithms.checkTriangleValidity(5,13,7))
if __name__ == '__main__':
    unittest.main()