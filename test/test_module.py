import sys

sys.path.append("..")
import unittest
from src.ClassFiles.PerangkatListrik import PerangkatListrik


class ModuleTesting(unittest.TestCase):
    def test_perangkat_listrik_default(self):
        # Test valid input
        perangkat_listrik = PerangkatListrik(1, False)
        self.assertEqual(
            perangkat_listrik.getDataPerangkatListrik(), (1, False, "", 0, 0, 0, 0)
        )

    def test_perangkat_listrik_defined(self):
        # Test valid input
        perangkat_listrik = PerangkatListrik(1, True, "Device-1", 100.0, 5.0, 220.0, 10)
        self.assertEqual(
            perangkat_listrik.getDataPerangkatListrik(),
            (1, True, "Device-1", 100.0, 5.0, 220.0, 10),
        )


if __name__ == "__main__":
    unittest.main()
