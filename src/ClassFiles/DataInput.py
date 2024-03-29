from src.ClassFiles.PerangkatListrik import PerangkatListrik


class DataInput1:
    def __init__(
        self,
        id: int,
        nama: str,
        daya: float,
        arus: float,
        tegangan: float,
        nama_ruangan: str,
    ):
        self.validate_user_input(id, nama, daya, arus, tegangan, nama_ruangan)

    def validate_user_input(
        self,
        id: int,
        nama: str,
        daya: float,
        arus: float,
        tegangan: float,
        nama_ruangan: str,
    ):
        if len(nama) == 0 or len(nama_ruangan) == 0:
            raise Exception("Nama perangkat listrik tidak boleh kosong!")
        self.id = id
        self.nama = nama
        self.daya = daya
        self.arus = arus
        self.tegangan = tegangan
        self.nama_ruangan = nama_ruangan

    # Getters
    def get_user_input(self):
        return (
            self.id,
            self.nama,
            self.daya,
            self.arus,
            self.tegangan,
            self.nama_ruangan,
        )

    def get_input_name(self):
        return self.nama

    def get_input_daya(self):
        return self.daya

    def get_input_arus(self):
        return self.arus

    def get_input_tegangan(self):
        return self.tegangan

    def get_nama_ruangan(self):
        return self.nama_ruangan

    def create_p_listrik(self):
        data = self.get_user_input()
        # Need to fecth database item here to create new id
        return PerangkatListrik(
            self.id, False, data[1], data[2], data[3], data[4], data[5]
        )


class DataInput2(DataInput1):
    def __init__(
        self,
        id: int,
        nama: str,
        daya: float,
        arus: float,
        tegangan: float,
        nama_ruangan: str,
        durasi: float,
    ):
        super().__init__(id, nama, daya, arus, tegangan, nama_ruangan)
        self.durasi = durasi

    def get_user_input(self):
        return (
            self.id,
            self.nama,
            self.daya,
            self.arus,
            self.tegangan,
            self.nama_ruangan,
            self.durasi,
        )

    def create_p_listrik(self):
        data = self.get_user_input()
        return PerangkatListrik(
            self.id, False, data[1], data[2], data[3], data[4], data[5], self.durasi
        )
