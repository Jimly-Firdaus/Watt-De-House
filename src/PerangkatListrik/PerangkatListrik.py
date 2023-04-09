# File PerangkatListrik.py


class PerangkatListrik:
    # Constructor
    def __init__(self):
        self.nama_p_listrik = ""
        self.daya_p_listrik = 0
        self.arus_p_listrik = 0
        self.tegangan_p_listrik = 0
        self.durasi_p_listrik = 0

    # Getter
    def getDataPerangkatListrik(self):
        return (
            self.nama_p_listrik,
            self.daya_p_listrik,
            self.arus_p_listrik,
            self.tegangan_p_listrik,
            self.durasi_p_listrik,
        )

    # Setter
    def setNamaPListrik(self, name):
        self.nama_p_listrik = name

    def setDayaPListrik(self, daya):
        self.daya_p_listrik = daya

    def setArusPListrik(self, arus):
        self.arus_p_listrik = arus

    def setTeganganPListrik(self, tegangan):
        self.tegangan_p_listrik = tegangan

    def setDurasiPListrik(self, durasi):
        self.durasi_p_listrik = durasi
