class Simulator:
    def __init__(
        self,
        maxPower,
        listRuangan,
        costEstimation,
        notifyButton,
    ):
        self.maxPower = maxPower
        self.electricalOverload = False
        self.listRuangan = listRuangan
        self.notifyButton = notifyButton
        self.costEstimation = costEstimation

    def changeProperties(self):
        self.electricalOverload = not (self.electricalOverload)

    def updateElectricalState(self):
        for ruangan in self.listRuangan:
            if ruangan.daya > self.maxPower:
                self.changeProperties(self)
                return True
        return False

    def stopSimulation(self):
        if self.notifyButton:
            del self

    def displaySimulation(self):
        for ruangan in self.listRuangan:
            print("All attribute")
        print(self.costEstimation)
