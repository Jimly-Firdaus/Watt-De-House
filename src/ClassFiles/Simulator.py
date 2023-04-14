from typing import List
from ClassFiles.Ruangan import Ruangan


class Simulator:
    def __init__(
        self,
        listRuangan: List[Ruangan],
        costEstimation,
        notifyButton,
    ):
        self.electricalOverload = False
        self.listRuangan = listRuangan
        self.notifyButton = notifyButton
        self.costEstimation = costEstimation

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
        print(self.costEstimation)
