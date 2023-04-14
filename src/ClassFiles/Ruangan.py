class Ruangan:
    def __init__(self, ListPerangkatListrikRuangan, maxPower):
        self.listPerangkatListrikRuangan = ListPerangkatListrikRuangan
        self.maxPower = maxPower

    def displayDataPerangkatListrikRuangan(self):
        print(self.listPerangkatListrikRuangan)

    def getMaxPower(self):
        return self.maxPower
