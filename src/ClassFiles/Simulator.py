from typing import List
from src.ClassFiles.Ruangan import Ruangan
from src.ClassFiles.Estimator import Estimator


class Simulator:
    def __init__(self,):
        self.electrical_overload = False
        self.notify_button = False

    def update_electrical_state(self, list_ruangan: List[Ruangan]):
        self.overloads_ruangan = []
        circuit_breaker_power = {}
        for ruangan in list_ruangan:
            if ruangan.have_circuit_breaker():
                circuit_breaker_name = ruangan.get_circuit_breaker_name()
                if circuit_breaker_name not in circuit_breaker_power:
                    circuit_breaker_power[circuit_breaker_name] = 0
                circuit_breaker_power[
                    circuit_breaker_name
                ] += ruangan.total_power_used()

        for ruangan in list_ruangan:
            if ruangan.have_circuit_breaker():
                circuit_breaker_name = ruangan.get_circuit_breaker_name()
                if (
                    circuit_breaker_power[circuit_breaker_name]
                    > ruangan.get_threshold()
                ):
                    self.overloads_ruangan.append(
                        (ruangan.get_ruangan_name(), True, True)
                    )

    def get_simulator_state(self, list_ruangan: List[Ruangan]):
        self.update_electrical_state(list_ruangan)
        if len(self.overloads_ruangan) != 0:
            return self.overloads_ruangan
        return []

    def stop_simulation(self):
        if self.notify_button:
            del self

    def get_estimator(self, list_ruangan: List[Ruangan]):
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
