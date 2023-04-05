import sys

sys.path.append("..")
import unittest
from src.main import pangkat2


class ModuleTesting(unittest.TestCase):
    def test_pangkat2(self):
        self.assertEqual(pangkat2(2), 4)


if __name__ == "__main__":
    unittest.main()
