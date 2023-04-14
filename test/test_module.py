import sys

sys.path.append("..")
import unittest
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from src.ClassFiles.Estimator import Estimator
from src.ClassFiles.Simulator import Simulator
from src.ClassFiles.Ruangan import Ruangan


class ModuleTesting(unittest.TestCase):
    def test_perangkat_listrik_default(self):
        # Test valid input
        perangkat_listrik = PerangkatListrik(1, False)
        self.assertEqual(
            perangkat_listrik.get_data_perangkat_listrik(), (1, False, "", 0, 0, 0, 0)
        )

    def test_perangkat_listrik_defined(self):
        # Test valid input
        perangkat_listrik = PerangkatListrik(1, True, "Device-1", 100.0, 5.0, 220.0, 10)
        self.assertEqual(
            perangkat_listrik.get_data_perangkat_listrik(),
            (1, True, "Device-1", 100.0, 5.0, 220.0, 10),
        )

    def test_Estimator_defined(self):
        # Test valid input
        perangkat_listrik1 = PerangkatListrik(
            1, True, "Device-1", 100.0, 5.0, 220.0, 10
        )
        perangkat_listrik2 = PerangkatListrik(
            2, True, "Device-2", 100.0, 5.0, 220.0, 10
        )
        listPerangkat = []
        listPerangkat.append(perangkat_listrik2)
        listPerangkat.append(perangkat_listrik1)
        Estimator1 = Estimator(True, listPerangkat)
        self.assertEqual(
            Estimator1.get_harga_listrik(),
            (605),
        )
        Estimator1.hitung_biaya_listrik()
        self.assertEqual(
            Estimator1.get_total_biaya(),
            (2 * 30 * 605),
        )

    def test_ruangan(self):
        list_perangkat_listrik = []
        for i in range(10):
            list_perangkat_listrik.append(
                PerangkatListrik(i, False, "Device-" + str(i), 100.0, 5.0, 220.0, 10)
            )
        test_nama_ruangan = "Test_Ruangan"
        ruangan = Ruangan(1, test_nama_ruangan, list_perangkat_listrik, True, 1000)
        self.assertEqual(
            (1, test_nama_ruangan, list_perangkat_listrik, True, 1000),
            ruangan.get_all_attributes(),
        )

    def test_simulator(self):
        perangkat_listrik1 = PerangkatListrik(1, "Device-1", 100.0, 5.0, 220.0, 10)
        perangkat_listrik2 = PerangkatListrik(2, "Device-2", 200.0, 5.0, 220.0, 10)
        perangkat_listrik3 = PerangkatListrik(3, "Device-3", 300.0, 5.0, 220.0, 10)
        perangkat_listrik4 = PerangkatListrik(4, "Device-4", 400.0, 5.0, 220.0, 10)
        perangkat_listrik5 = PerangkatListrik(5, "Device-5", 500.0, 5.0, 220.0, 10)
        perangkat_listrik6 = PerangkatListrik(6, "Device-6", 300.0, 5.0, 220.0, 10)
        perangkat_listrik7 = PerangkatListrik(7, "Device-7", 100.0, 5.0, 220.0, 10)
        perangkat_listrik8 = PerangkatListrik(8, "Device-8", 100.0, 5.0, 220.0, 10)
        perangkat_listrik9 = PerangkatListrik(9, "Device-9", 50.0, 5.0, 220.0, 10)
        perangkat_listrik10 = PerangkatListrik(10, "Device-10", 250.0, 5.0, 220.0, 10)
        list_perangkat_listrik1 = [
            perangkat_listrik1,
            perangkat_listrik2,
            perangkat_listrik3,
            perangkat_listrik4,
        ]
        list_perangkat_listrik2 = [
            perangkat_listrik5,
            perangkat_listrik6,
            perangkat_listrik7,
            perangkat_listrik8,
        ]
        list_perangkat_listrik3 = [perangkat_listrik9, perangkat_listrik10]
        ruangan1 = Ruangan("Ruangan-1", list_perangkat_listrik1, True, 900, 1)
        ruangan2 = Ruangan("Ruangan-2", list_perangkat_listrik2, True, 1000, 1)
        ruangan3 = Ruangan("Ruangan-3", list_perangkat_listrik3, False, 1000, 1)
        list_ruangan = [ruangan1, ruangan2, ruangan3]
        simulator = Simulator(list_ruangan)
        self.assertEqual(simulator.get_data_simulator(), (list_ruangan, False, False))


if __name__ == "__main__":
    unittest.main()
