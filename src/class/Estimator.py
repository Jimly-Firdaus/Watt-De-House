class Estimator:
    def __init__(self, hargaListrik, showTotalConsumption, listPerangkatListrik):
        self.hargaListrik = hargaListrik
        self.showTotalConsumption = showTotalConsumption
        self.listPerangkatListrik = listPerangkatListrik
        self.totalBiaya = 0

    def __init__(self, showTotalConsumption, listPerangkatListrik):
        self.showTotalConsumption = showTotalConsumption
        self.hargaListrik = 605  # asumsi daya 900VA dan bersubsidi
        self.listPerangkatListrik = listPerangkatListrik
        self.totalBiaya = 0

    def getHargaListrik(self):
        return self.hargaListrik

    def setHargaListrik(self, hargaListrik):
        self.hargaListrik = hargaListrik

    def hitungBiayaListrik(self):
        for i in range(len(self.listPerangkatListrik)):
            self.totalBiaya += (
                self.listPerangkatListrik[i].daya_p_listrik
                * self.listPerangkatListrik[i].durasi
            )
        self.totalBiaya *= self.hargaListrik

    def displayTotalBIaya(self):
        print("Total Biaya :" + self.totalBiaya)

    def showConsumption(self):
        if self.showTotalConsumption == True:
            for perangkatListrik in self.listPerangkatListrik:
                biaya = (
                    perangkatListrik.daya_p_listrik
                    * perangkatListrik.durasi
                    * self.hargaListrik
                )
                print(perangkatListrik.nama_p_listrik + " : " + biaya)
