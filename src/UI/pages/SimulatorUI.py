import sys

sys.path.insert(0, "../../")
from components.FeatureButton import FeatureButton
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtCore
from typing import List
from src.ClassFiles.Ruangan import Ruangan


class Simulator(PageWindow):
    # TODO: Circuit Breaker and overloads detection
    def __init__(self, list_of_ruangan: List[Ruangan]):
        super().__init__()
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
        self.estimate_result = QtWidgets.QLabel("Estimated: 1000")
        header.addWidget(self.estimate_result)
        header.addStretch()

        self.backButton = UtilityButton("Back", lambda: self.back_to_main(), self)
        self.backButton.setMinimumSize(90, 90)
        header.addWidget(self.backButton)
        main_layout.addLayout(header)

        # Main content section
        h_layout = QtWidgets.QHBoxLayout()
        # Loop each ruangan
        for ruangan in list_of_ruangan:
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

        main_layout.addLayout(h_layout)

    # Callback fn
    def back_to_main(self):
        self.goto("main")

    def update_state_perangkat(self, perangkat, state):
        print("Changed something!")
        perangkat.set_status_p_listrik(state == QtCore.Qt.Checked)
