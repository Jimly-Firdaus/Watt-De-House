class PerangkatListrik:
    # Constructor
    def __init__(
        self,
        id,
        nama: str = "",
        daya: float = 0,
        arus: float = 0,
        tegangan: float = 0,
        durasi: int = 0,
    ):
        self.id_perangkat_listrik = id
        self.nama_p_listrik = nama
        self.daya_p_listrik = daya
        self.arus_p_listrik = arus
        self.tegangan_p_listrik = tegangan
        self.durasi_p_listrik = durasi

    # Getter
    def getDataPerangkatListrik(self):
        return (
            self.id,
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

    def setIdPListrik(self, o):
        self.id = o
