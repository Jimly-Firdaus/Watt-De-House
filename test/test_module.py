# import sys

# sys.path.insert(0, "../")
import unittest
from src.ClassFiles.Database import Database
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from src.ClassFiles.Estimator import Estimator
from src.ClassFiles.Simulator import Simulator
from src.ClassFiles.Ruangan import Ruangan
from src.ClassFiles.DataInput import DataInput1, DataInput2
from src import main


class ModuleTesting(unittest.TestCase):
    def setUp(self):
        self.db = Database("test.db")

    def tearDown(self):
        self.db.close()

    def test_database_operations(self):
        with self.subTest("Insert data"):
            self.db.create_table(
                "test_table",
                {
                    "nama": "text",
                    "daya": "real",
                    "arus": "real",
                    "tegangan": "real",
                    "durasi": "integer",
                },
            )
            self.db.insert_data(
                "test_table",
                {
                    "nama": "device-1",
                    "daya": 100.0,
                    "arus": 12.0,
                    "tegangan": 220.0,
                    "durasi": 120,
                },
            )
            data = self.db.get_data("test_table")
            expected_data = [("device-1", 100.0, 12.0, 220.0, 120)]
            self.assertEqual(data, expected_data)

        with self.subTest("Update data"):
            self.db.update_data(
                "test_table", {"nama": "device-2"}, {"nama": "device-1"}
            )
            data = self.db.get_data("test_table")
            expected_data = [("device-2", 100.0, 12.0, 220.0, 120)]
            self.assertEqual(data, expected_data)

        with self.subTest("Delete data"):
            self.db.delete_data("test_table", {"arus": 12.0})
            data = self.db.get_data("test_table")
            expected_data = []
            self.assertEqual(data, expected_data)

    def test_data_input_1(self):
        # Test valid input
        data_input = DataInput1(0, "Device-1", 100.0, 5.0, 220.0, "Ruangan-1")
        self.assertEqual(
            data_input.get_user_input(), (0, "Device-1", 100.0, 5.0, 220.0, "Ruangan-1")
        )
        perangkat_listrik = data_input.create_p_listrik()
        perangkat_listrik_expected = PerangkatListrik(
            0, False, "Device-1", 100.0, 5.0, 220.0, "Ruangan-1"
        )
        self.assertEqual(
            perangkat_listrik.get_data_perangkat_listrik(),
            perangkat_listrik_expected.get_data_perangkat_listrik(),
        )
        # Test invalid input
        with self.assertRaises(Exception):
            data_input = DataInput1(1, "", 100.0, 5.0, 220.0, "Ruangan-1")

    def test_data_input_2(self):
        # Test valid input
        data_input = DataInput2(0, "Device-2", 100.0, 5.0, 220.0, "Ruangan-2", 10)
        self.assertEqual(
            data_input.get_user_input(),
            (0, "Device-2", 100.0, 5.0, 220.0, "Ruangan-2", 10),
        )
        perangkat_listrik = data_input.create_p_listrik()
        perangkat_listrik_expected = PerangkatListrik(
            0, False, "Device-2", 100.0, 5.0, 220.0, "Ruangan-2", 10
        )
        self.assertEqual(
            perangkat_listrik.get_data_perangkat_listrik(),
            perangkat_listrik_expected.get_data_perangkat_listrik(),
        )

    def test_perangkat_listrik_default(self):
        # Test valid input
        perangkat_listrik = PerangkatListrik(1, False)
        self.assertEqual(
            perangkat_listrik.get_data_perangkat_listrik(),
            (1, False, "", 0, 0, 0, "", 0),
        )

    def test_perangkat_listrik_defined(self):
        # Test valid input
        perangkat_listrik = PerangkatListrik(
            1, True, "Device-1", 100.0, 5.0, 220.0, "Ruangan-2", 10
        )
        self.assertEqual(
            perangkat_listrik.get_data_perangkat_listrik(),
            (1, True, "Device-1", 100.0, 5.0, 220.0, "Ruangan-2", 10),
        )

    def test_Estimator_defined(self):
        # Test valid input
        perangkat_listrik1 = PerangkatListrik(
            1, True, "Device-1", 100.0, 5.0, 220.0, "Ruangan-2", 10
        )
        perangkat_listrik2 = PerangkatListrik(
            2, True, "Device-2", 100.0, 5.0, 220.0, "Ruangan-2", 10
        )
        listPerangkat = []
        listPerangkat.append(perangkat_listrik2)
        listPerangkat.append(perangkat_listrik1)
        Estimator1 = Estimator(True, listPerangkat, 605)
        self.assertEqual(
            Estimator1.get_harga_listrik(),
            (605),
        )
        self.assertEqual(
            Estimator1.get_total_biaya(),
            (2 * 30 * 605),
        )

    def test_ruangan(self):
        list_perangkat_listrik = []
        for i in range(10):
            list_perangkat_listrik.append(
                PerangkatListrik(
                    i, False, "Device-" + str(i), 100.0, 5.0, 220.0, "Ruangan-2", 10
                )
            )
        test_nama_ruangan = "Test_Ruangan"
        ruangan = Ruangan(
            1, test_nama_ruangan, list_perangkat_listrik, True, "Circuit-Breaker", 1000
        )
        self.assertEqual(
            (
                1,
                test_nama_ruangan,
                list_perangkat_listrik,
                True,
                "Circuit-Breaker",
                1000,
            ),
            ruangan.get_all_attributes(),
        )

    def test_run_gui(self):
        try:
            app = main.run_app()
            app.quit()
        except Exception as e:
            self.fail(f"Running the app raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
