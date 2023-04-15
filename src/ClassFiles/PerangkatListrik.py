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
    def get_data_perangkat_listrik(self):
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
    def set_nama_p_listrik(self, name):
        self.nama_p_listrik = name

    def set_daya_p_listrik(self, daya):
        self.daya_p_listrik = daya

    def set_arus_p_listrik(self, arus):
        self.arus_p_listrik = arus

    def set_tegangan_p_listrik(self, tegangan):
        self.tegangan_p_listrik = tegangan

    def set_durasi_p_listrik(self, durasi):
        self.durasi_p_listrik = durasi

    def set_id_p_listrik(self, id):
        self.id_p_listrik = id

    def set_status_p_listrik(self, status):
        self.is_active_p_listrik = status
