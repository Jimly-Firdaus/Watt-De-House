import sys

sys.path.append("..")
import unittest
from src.ClassFiles.Database import Database


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


if __name__ == "__main__":
    unittest.main()
