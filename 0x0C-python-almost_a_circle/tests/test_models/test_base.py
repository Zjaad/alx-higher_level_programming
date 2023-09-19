# alx-higher_level_programming/0x0C-python-almost_a_circle/tests/test_models/test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_none(self):
        """Test creating a Base instance with id=None."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_positive(self):
        """Test creating a Base instance with a positive id."""
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_id_zero(self):
        """Test creating a Base instance with id=0."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test creating a Base instance with a negative id."""
        b = Base(-10)
        self.assertEqual(b.id, -10)

    def test_id_string(self):
        """Test creating a Base instance with id as a string."""
        b = Base("test")
        self.assertEqual(b.id, "test")

if __name__ == '__main__':
    unittest.main()
