from typing import List
from ClassFiles.PerangkatListrik import PerangkatListrik


class Ruangan:
    def __init__(
        self,
        nama_ruangan: str,
        list_perangkat_listrik_ruangan: List[PerangkatListrik],
        circuit_breaker: bool,
        threshold: float,
        id: int,
    ):
        self.id = id
        self.nama_ruangan = nama_ruangan
        self.list_perangkat_listrik_ruangan = list_perangkat_listrik_ruangan
        self.avail_circuit_breaker = circuit_breaker
        self.circuit_breaker_threshold = threshold

    def displayDataPerangkatListrikRuangan(self):
        print(self.list_perangkat_listrik_ruangan)

    def getRuanganName(self):
        return self.nama_ruangan

    def getListPerangkatListrik(self):
        return self.list_perangkat_listrik_ruangan

    def haveCircuitBreaker(self):
        return self.avail_circuit_breaker

    def getThreshold(self):
        if self.avail_circuit_breaker:
            return self.circuit_breaker_threshold
        return -1

    def getMaxPower(self):
        return self.max_power

    def setThreshold(self, o):
        if self.avail_circuit_breaker:
            self.circuit_breaker_threshold = o

    def changeCircuitBreakerStatus(self, status):
        self.avail_circuit_breaker = status

    def addPerangkatListrik(self, perangkat_listrik: PerangkatListrik):
        self.list_perangkat_listrik_ruangan.append(perangkat_listrik)

    def removePerangkatListirk(self, nama_perangkat: str, id: int):
        for pl in self.list_perangkat_listrik_ruangan:
            data = pl.getDataPerangkatListrik()
            if data[0] == id and data[1] == nama_perangkat:
                self.list_perangkat_listrik_ruangan.remove(pl)
                break
