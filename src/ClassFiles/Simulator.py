from typing import List
from src.ClassFiles.Ruangan import Ruangan
from src.ClassFiles.Estimator import Estimator


class Simulator:
    def __init__(
        self,
        list_ruangan: List[Ruangan],
    ):
        self.electrical_overload = False
        self.list_ruangan = list_ruangan
        self.notify_button = False

    def change_properties(self):
        self.electrical_overload = not (self.electrical_overload)

    def update_electrical_state(self):
        for ruangan in self.list_ruangan:
            if ruangan.total_power_used() > ruangan.get_threshold():
                self.change_properties(self)
                return True
        return False

    def stop_simulation(self):
        if self.notify_button:
            del self

    def display_simulation(self):
        for ruangan in self.list_ruangan:
            ruangan.display_data_perangkat_listrik_ruangan()
            list_perangkat_listrik_ruangan = ruangan.get_list_perangkat_listrik()
            active_pl = []
            for pl in list_perangkat_listrik_ruangan:
                data = pl.get_data_perangkat_listrik()
                if data[1]:
                    active_pl.append(pl)
            estimator_ruangan = Estimator(True, active_pl)
            print(estimator_ruangan)

    def change_notify_button(self):
        self.notify_button = True

    def get_data_simulator(self):
        return (
            self.list_ruangan,
            self.electrical_overload,
            self.notify_button,
        )
