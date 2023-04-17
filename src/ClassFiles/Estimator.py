from typing import List
from src.ClassFiles.PerangkatListrik import PerangkatListrik


class Estimator:
    def __init__(
        self,
        showTotalConsumption: bool,
        listPerangkatListrik: List[PerangkatListrik],
        hargaListrik: float,  # asumsi daya 900VA dan bersubsidi
    ):
        self.showTotalConsumption = showTotalConsumption
        self.listPerangkatListrik = listPerangkatListrik
        self.hargaListrik = hargaListrik
        self.totalBiaya = 0

    def get_harga_listrik(self):
        return self.hargaListrik

    def set_harga_listrik(self, hargaListrik):
        self.hargaListrik = hargaListrik

    def get_total_biaya(self):
        self.hitung_biaya_listrik()
        return self.totalBiaya

    def hitung_biaya_listrik(self):
        for i in range(len(self.listPerangkatListrik)):
            self.totalBiaya += (
                self.listPerangkatListrik[i].daya_p_listrik
                * 30
                * self.listPerangkatListrik[i].durasi_p_listrik
                / 1000
            )
        self.totalBiaya *= self.hargaListrik

    def display_total_biaya(self):
        return "Total Biaya :" + str(self.totalBiaya)

    def show_consumption(self):
        if self.showTotalConsumption == True:
            for perangkatListrik in self.listPerangkatListrik:
                biaya = (
                    perangkatListrik.daya_p_listrik
                    * perangkatListrik.durasi_p_listrik
                    * self.hargaListrik
                )
                print(perangkatListrik.nama_p_listrik + " : " + biaya)
