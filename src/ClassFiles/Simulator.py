from typing import List
from src.ClassFiles.Ruangan import Ruangan
from src.ClassFiles.Estimator import Estimator


class Simulator:
    def __init__(
        self,
    ):
        self.electrical_overload = False
        self.notify_button = False

    def update_electrical_state(self, list_ruangan):
        self.overloads_ruangan = []
        for ruangan in list_ruangan:
            if ruangan.total_power_used() > ruangan.get_threshold():
                self.overloads_ruangan.append(ruangan.get_ruangan_name())

    def get_simulator_state(self, list_ruangan):
        self.update_electrical_state(list_ruangan)
        if len(self.overloads_ruangan) != 0:
            return (True, self.overloads_ruangan)
        return (False, self.overloads_ruangan)

    def stop_simulation(self):
        if self.notify_button:
            del self

    def get_estimator(self, list_ruangan):
        list_estimator = []
        for ruangan in list_ruangan:
            list_perangkat_listrik_ruangan = ruangan.get_list_perangkat_listrik()
            active_pl = []
            for pl in list_perangkat_listrik_ruangan:
                data = pl.get_data_perangkat_listrik()
                if data[1]:
                    active_pl.append(pl)
            estimator_ruangan = Estimator(True, active_pl)
            list_estimator.append(estimator_ruangan)
        return list_estimator

    def change_notify_button(self):
        self.notify_button = True

    def get_data_simulator(self):
        return (
            self.electrical_overload,
            self.notify_button,
        )
