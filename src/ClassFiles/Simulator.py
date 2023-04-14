from typing import List
from src.ClassFiles.Ruangan import Ruangan
from src.ClassFiles.Estimator import Estimator


class Simulator:
    def __init__(
        self,
        listRuangan: List[Ruangan],
    ):
        self.electricalOverload = False
        self.listRuangan = listRuangan
        self.notifyButton = False

    def changeProperties(self):
        self.electricalOverload = not (self.electricalOverload)

    def updateElectricalState(self):
        for ruangan in self.listRuangan:
            if ruangan.totalPowerUsed() > ruangan.getThreshold():
                self.changeProperties(self)
                return True
        return False

    def stopSimulation(self):
        if self.notifyButton:
            del self

    def displaySimulation(self):
        for ruangan in self.listRuangan:
            ruangan.displayDataPerangkatListrikRuangan()
            list_perangkat_listrik_ruangan = ruangan.getListPerangkatListrik()
            active_pl = []
            for pl in list_perangkat_listrik_ruangan:
                data = pl.getDataPerangkatListrik()
                if data[1]:
                    active_pl.append(pl)
            estimator_ruangan = Estimator(True, active_pl)
            print(estimator_ruangan)

    def changeNotifyButton(self):
        self.notifyButton = True

    def getDataSimulator(self):
        return (
            self.listRuangan,
            self.electricalOverload,
            self.notifyButton,
        )
