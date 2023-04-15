import sys

sys.path.insert(0, "../../")
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtCore
from typing import List
from src.ClassFiles.Ruangan import Ruangan
from src.ClassFiles.Simulator import Simulator


class SimulatorPage(PageWindow):
    def __init__(self, list_of_ruangan: List[Ruangan]):
        super().__init__()
        self.simulator = Simulator()
        self.list_ruangan = list_of_ruangan
        self.circuit_breaker_boxes = {}

        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #FFFFFF;")
        self.setWindowTitle("Simulator")

        # Create a scroll area
        scroll_area = QtWidgets.QScrollArea()
        self.setCentralWidget(scroll_area)

        # Create a widget to hold our layout
        widget = QtWidgets.QWidget()
        scroll_area.setWidget(widget)
        scroll_area.setWidgetResizable(True)

        # Create a horizontal layout
        main_layout = QtWidgets.QVBoxLayout(widget)

        # Header section
        header = QtWidgets.QHBoxLayout()
        v1_layout = QtWidgets.QVBoxLayout()
        self.overloads_view = QtWidgets.QLabel("Overloads status: Safe")
        v1_layout.addWidget(self.overloads_view)
        self.overloaded_ruangan = QtWidgets.QLabel("Overloaded Ruangan: Tidak ada")
        v1_layout.addWidget(self.overloaded_ruangan)
        header.addLayout(v1_layout)
        header.addStretch()

        self.backButton = UtilityButton("Back", lambda: self.back_to_main(), self)
        self.backButton.setMinimumSize(90, 90)
        header.addWidget(self.backButton)
        main_layout.addLayout(header)

        # Main content section
        h_layout = QtWidgets.QHBoxLayout()
        # Loop each ruangan
        for ruangan in self.list_ruangan:
            # Group box for the Ruangan
            group_box = QtWidgets.QGroupBox(ruangan.get_ruangan_name())
            h_layout.addWidget(group_box)

            # Vertical layout for the Perangkat
            v_layout = QtWidgets.QVBoxLayout(group_box)

            # Append Perangkat to the layout
            for perangkat in ruangan.get_list_perangkat_listrik():
                data = perangkat.get_data_perangkat_listrik()
                check_box = QtWidgets.QCheckBox(data[2])
                check_box.setChecked(data[1])
                check_box.stateChanged.connect(
                    lambda state, p=perangkat: self.update_state_perangkat(p, state)
                )
                v_layout.addWidget(check_box)
            if ruangan.have_circuit_breaker():
                circuit_breaker_box = QtWidgets.QCheckBox(
                    ruangan.get_circuit_breaker_name()
                )
                circuit_breaker_box.setChecked(False)
                circuit_breaker_box.setEnabled(False)
                self.circuit_breaker_boxes[
                    ruangan.get_ruangan_name()
                ] = circuit_breaker_box
                v_layout.addWidget(circuit_breaker_box)
        main_layout.addLayout(h_layout)

    # Callback fn
    def back_to_main(self):
        self.goto("main")

    @QtCore.pyqtSlot(object, int)
    def update_state_perangkat(self, perangkat, state):
        print("Changed something!")
        perangkat.set_status_p_listrik(state == QtCore.Qt.Checked)
        state_ruangan = self.simulator.get_simulator_state(self.list_ruangan)

        # Reset circuit breaker
        for circuit_breaker_box in self.circuit_breaker_boxes.values():
            circuit_breaker_box.setChecked(False)

        overloaded_ruangan = ""
        if len(state_ruangan) != 0:
            self.overloads_view.setText(
                "Overloads status: Potential Electrical Overloads!"
            )
            for ruangan, overloads, circuit_breaker in state_ruangan:
                overloaded_ruangan += ruangan + ", "
                if overloads == True:
                    circuit_breaker_name = self.circuit_breaker_boxes[ruangan].text()
                    for circuit_breaker_box in self.circuit_breaker_boxes.values():
                        if circuit_breaker_box.text() == circuit_breaker_name:
                            circuit_breaker_box.setChecked(True)
            self.overloaded_ruangan.setText(
                "Overloaded Ruangan: " + overloaded_ruangan[:-2]
            )
        else:
            self.overloads_view.setText("Overloads status: Safe")
            self.overloaded_ruangan.setText("Overloaded Ruangan: Tidak ada")
