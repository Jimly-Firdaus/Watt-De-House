import sys

sys.path.insert(0, "../../")
from typing import List
from src.ClassFiles.Database import Database
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from src.ClassFiles.Ruangan import Ruangan


class Util:
    @staticmethod
    def get_all_ruangan(db: Database):
        ruangan_rows = db.get_data("ruangan")
        ruangan_list = []
        for row in ruangan_rows:
            id, nama_ruangan, circuit_breaker, circuit_breaker_name, threshold = row
            perangkat_listrik_rows = db.get_data(
                "perangkat_listrik",
                condition={
                    "id": (
                        f"SELECT id_perangkat_listrik FROM ruangan_perangkat_listrik WHERE id_ruangan = {id}"
                    )
                },
            )
            list_perangkat_listrik_ruangan = []
            for pl_row in perangkat_listrik_rows:
                pl_id, status, nama, daya, arus, tegangan, durasi = pl_row
                perangkat_listrik = PerangkatListrik(
                    pl_id, status, nama, daya, arus, tegangan, durasi
                )
                list_perangkat_listrik_ruangan.append(perangkat_listrik)
            ruangan = Ruangan(
                id,
                nama_ruangan,
                list_perangkat_listrik_ruangan,
                bool(circuit_breaker),
                circuit_breaker_name,
                threshold,
            )
            ruangan_list.append(ruangan)
        return ruangan_list

    @staticmethod
    def store_to_db(db: Database, list_ruangan: List[Ruangan]):
        for ruangan in list_ruangan:
            db.insert_data(
                "ruangan",
                {
                    "id": ruangan.id,
                    "nama_ruangan": ruangan.nama_ruangan,
                    "circuit_breaker": int(ruangan.circuit_breaker),
                    "circuit_breaker_name": ruangan.circuit_breaker_name,
                    "threshold": ruangan.threshold,
                },
            )
        for perangkat_listrik in ruangan.list_perangkat_listrik_ruangan:
            db.insert_data(
                "perangkat_listrik",
                {
                    "id": perangkat_listrik.id,
                    "status": perangkat_listrik.status,
                    "nama": perangkat_listrik.nama,
                    "daya": perangkat_listrik.daya,
                    "arus": perangkat_listrik.arus,
                    "tegangan": perangkat_listrik.tegangan,
                    "durasi": perangkat_listrik.durasi,
                },
            )
            db.insert_data(
                "ruangan_perangkat_listrik",
                {
                    "id_ruangan": ruangan.id,
                    "id_perangkat_listrik": perangkat_listrik.id,
                },
            )
