# File PerangkatListrik.py


class PerangkatListrik:
    # Constructor
    def __init__(self):
        self.nama_p_listrik = ""
        self.daya_p_listrik = 0
        self.arus_p_listrik = 0
        self.tegangan_p_listrik = 0
        self.durasi_p_listrik = 0

    def __init__(
        self, nama: str, daya: float, arus: float, tegangan: float, durasi: int = 0
    ):
        self.nama_p_listrik = nama
        self.daya_p_listrik = daya
        self.arus_p_listrik = arus
        self.tegangan_p_listrik = tegangan
        self.durasi_p_listrik = durasi

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
