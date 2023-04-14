import sys

sys.path.append("..")
import unittest
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from src.ClassFiles.Estimator import Estimator


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

    def test_Estimator_defined(self):
        # Test valid input
        perangkat_listrik1 = PerangkatListrik(1, "Device-1", 100.0, 5.0, 220.0, 10)
        perangkat_listrik2 = PerangkatListrik(2, "Device-2", 100.0, 5.0, 220.0, 10)
        listPerangkat = []
        listPerangkat.append(perangkat_listrik2)
        listPerangkat.append(perangkat_listrik1)
        Estimator1 = Estimator(True, listPerangkat)
        self.assertEqual(
            Estimator1.getHargaListrik(),
            (605),
        )
        Estimator1.hitungBiayaListrik()
        self.assertEqual(
            Estimator1.getTotalBiaya(),
            (2 * 30 * 605),
        )


if __name__ == "__main__":
    unittest.main()
