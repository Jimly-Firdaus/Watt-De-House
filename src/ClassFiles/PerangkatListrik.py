class PerangkatListrik:
    # Constructor
    def __init__(
        self,
        id,
        status,
        nama: str = "",
        daya: float = 0,
        arus: float = 0,
        tegangan: float = 0,
        durasi: int = 0,
    ):
        self.id_p_listrik = id
        self.is_active_p_listrik = status
        self.nama_p_listrik = nama
        self.daya_p_listrik = daya  # Power in watts
        self.arus_p_listrik = arus
        self.tegangan_p_listrik = tegangan
        self.durasi_p_listrik = durasi  # Duration in hours

    # Getter
    def getDataPerangkatListrik(self):
        return (
            self.id_p_listrik,
            self.is_active_p_listrik,
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

    def setIdPListrik(self, id):
        self.id_p_listrik = id

    def setStatusPListrik(self, status):
        self.is_active_p_listrik = status
