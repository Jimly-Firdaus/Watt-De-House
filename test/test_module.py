import sys

sys.path.append("..")
import unittest
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from src.ClassFiles.DataInput import DataInput1, DataInput2


class ModuleTesting(unittest.TestCase):
    def test_data_input_1(self):
        # Test valid input
        data_input = DataInput1("Device-1", 100.0, 5.0, 220.0)
        self.assertEqual(data_input.get_user_input(), ("Device-1", 100.0, 5.0, 220.0))

        # Test invalid input
        with self.assertRaises(Exception):
            data_input = DataInput1("", 100.0, 5.0, 220.0)

    def test_data_input_2(self):
        # Test valid input
        data_input = DataInput2("Device-2", 100.0, 5.0, 220.0, 10)
        self.assertEqual(
            data_input.get_user_input(), ("Device-2", 100.0, 5.0, 220.0, 10)
        )

        # Test invalid input
        with self.assertRaises(Exception):
            data_input = DataInput2("Device-2", 100.0, 5.0, 220.0, -1)

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
