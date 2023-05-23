import sys

sys.path.insert(0, "../../")
from typing import List
from ClassFiles.Database import Database
from ClassFiles.PerangkatListrik import PerangkatListrik
from ClassFiles.Ruangan import Ruangan


class Util:
    db_length = 0

    @staticmethod
    def get_all_data(db: Database):
        ruangan_rows = db.get_data("ruangan")
        ruangan_list = []
        all_perangkat_listrik = []
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
                pl_id, status, nama, daya, arus, tegangan, nama_ruangan, durasi = pl_row
                perangkat_listrik = PerangkatListrik(
                    pl_id, status, nama, daya, arus, tegangan, nama_ruangan, durasi
                )
                list_perangkat_listrik_ruangan.append(perangkat_listrik)
                all_perangkat_listrik.append(perangkat_listrik)
            ruangan = Ruangan(
                id,
                nama_ruangan,
                list_perangkat_listrik_ruangan,
                bool(circuit_breaker),
                circuit_breaker_name,
                threshold,
            )
            ruangan_list.append(ruangan)
        Util.db_length = len(ruangan_list)
        return (ruangan_list, all_perangkat_listrik)

    @staticmethod
    def store_to_db(db: Database, list_ruangan: List[Ruangan]):
        if Util.db_length != len(list_ruangan):
            for ruangan in list_ruangan:
                db.insert_data(
                    "ruangan",
                    {
                        "id": ruangan.id,
                        "nama_ruangan": ruangan.nama_ruangan,
                        "circuit_breaker": int(ruangan.avail_circuit_breaker),
                        "circuit_breaker_name": ruangan.circuit_breaker_name,
                        "threshold": ruangan.circuit_breaker_threshold,
                    },
                )
                for perangkat_listrik in ruangan.list_perangkat_listrik_ruangan:
                    db.insert_data(
                        "perangkat_listrik",
                        {
                            "id": perangkat_listrik.id_p_listrik,
                            "status": int(perangkat_listrik.is_active_p_listrik),
                            "nama": perangkat_listrik.nama_p_listrik,
                            "daya": perangkat_listrik.daya_p_listrik,
                            "arus": perangkat_listrik.arus_p_listrik,
                            "tegangan": perangkat_listrik.tegangan_p_listrik,
                            "nama_ruangan": perangkat_listrik.nama_ruangan,
                            "durasi": perangkat_listrik.durasi_p_listrik,
                        },
                    )
                    db.insert_data(
                        "ruangan_perangkat_listrik",
                        {
                            "id_ruangan": ruangan.id,
                            "id_perangkat_listrik": perangkat_listrik.id_p_listrik,
                        },
                    )
