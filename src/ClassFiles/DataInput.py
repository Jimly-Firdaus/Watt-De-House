from src.interface.IDataInput import *


class DataInput1(IDataInput):
    def __init__(self, nama: str, daya: float, arus: float, tegangan: float):
        self.validate_user_input(nama, daya, arus, tegangan)

    def validate_user_input(self, nama: str, daya: float, arus: float, tegangan: float):
        if len(nama) == 0:
            raise Exception("Nama perangkat listrik tidak boleh kosong!")
        if daya <= 0:
            raise Exception("Daya tidak boleh < 0 atau sama dengan 0!")
        if arus <= 0:
            raise Exception("Arus tidak boleh < 0 atau sama dengan 0!")
        if tegangan <= 0:
            raise Exception("Tegangan tidak boleh < 0 atau sama dengan 0!")
        self.nama = nama
        self.daya = daya
        self.arus = arus
        self.tegangan = tegangan

    # Getters
    def get_user_input(self):
        return (self.nama, self.daya, self.arus, self.tegangan)

    def get_input_name(self):
        return self.nama

    def get_input_daya(self):
        return self.daya

    def get_input_arus(self):
        return self.arus

    def get_input_tegangan(self):
        return self.tegangan


class DataInput2(DataInput1):
    def __init__(
        self, nama: str, daya: float, arus: float, tegangan: float, durasi: int
    ):
        super().__init__(nama, daya, arus, tegangan)
        if durasi < 0:
            raise Exception("Durasi tidak boleh < 0")
        self.durasi = durasi

    def get_user_input(self):
        return (self.nama, self.daya, self.arus, self.tegangan, self.durasi)
