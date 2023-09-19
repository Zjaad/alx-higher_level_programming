# alx-higher_level_programming/0x0C-python-almost_a_circle/tests/test_models/test_rectangle.py

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        """Test initializing a Rectangle."""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

    def test_area(self):
        """Test calculating the area of a Rectangle."""
        r = Rectangle(3, 7)
        self.assertEqual(r.area(), 21)

    def test_display(self):
        """Test displaying a Rectangle."""
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test the string representation of a Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

if __name__ == '__main__':
    unittest.main()
