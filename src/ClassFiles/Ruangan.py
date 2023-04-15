from typing import List
from src.ClassFiles.PerangkatListrik import PerangkatListrik


class Ruangan:
    def __init__(
        self,
        id: int,
        nama_ruangan: str,
        list_perangkat_listrik_ruangan: List[PerangkatListrik],
        circuit_breaker: bool,
        threshold: float,
    ):
        self.id = id
        self.nama_ruangan = nama_ruangan
        self.list_perangkat_listrik_ruangan = list_perangkat_listrik_ruangan
        self.avail_circuit_breaker = circuit_breaker
        self.circuit_breaker_threshold = threshold

    def display_data_perangkat_listrik_ruangan(self):
        print(self.list_perangkat_listrik_ruangan)

    def get_ruangan_name(self):
        return self.nama_ruangan

    def get_list_perangkat_listrik(self):
        return self.list_perangkat_listrik_ruangan

    def have_circuit_breaker(self):
        return self.avail_circuit_breaker

    def get_threshold(self):
        if self.avail_circuit_breaker:
            return self.circuit_breaker_threshold
        return -1

    def set_threshold(self, o):
        if self.avail_circuit_breaker:
            self.circuit_breaker_threshold = o

    def change_circuit_breaker_status(self, status):
        self.avail_circuit_breaker = status

    def add_perangkat_listrik(self, perangkat_listrik: PerangkatListrik):
        self.list_perangkat_listrik_ruangan.append(perangkat_listrik)

    def remove_perangkat_listirk(self, nama_perangkat: str, id: int):
        for pl in self.list_perangkat_listrik_ruangan:
            data = pl.get_data_perangkat_listrik()
            if data[0] == id and data[2] == nama_perangkat:
                self.list_perangkat_listrik_ruangan.remove(pl)
                break

    def total_power_used(self):
        power_used = 0
        for pl in self.list_perangkat_listrik_ruangan:
            data = pl.get_data_perangkat_listrik()
            if data[1]:
                power_used += data[3]
        return power_used

    def get_all_attributes(self):
        return (
            self.id,
            self.nama_ruangan,
            self.list_perangkat_listrik_ruangan,
            self.avail_circuit_breaker,
            self.circuit_breaker_threshold,
        )
