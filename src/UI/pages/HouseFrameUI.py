import sys

sys.path.insert(0, "../../")
from UI.components.StepButton import StepButton
from UI.components.UtilityButton import UtilityButton
from UI.util.PageWindow import PageWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from typing import List
from ClassFiles.PerangkatListrik import PerangkatListrik
from ClassFiles.Ruangan import Ruangan


class HouseFrame(PageWindow):
    list_ruangan_updated = pyqtSignal(list)

    def __init__(
        self,
        list_of_data: List[PerangkatListrik] = [],
        list_ruangan: List[Ruangan] = [],
    ):
        super().__init__()
        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #0B2447;")
        self.setWindowTitle("House Frame")
        self.circuit_breaker_info = []
        self.list_perangkat_listrik = list_of_data
        self.list_ruangan = list_ruangan
        self.id_ruangan = len(self.list_ruangan) + 1
        self.distinct_pl = set()
        self.distinct_room_name = set()
        print(len(self.list_ruangan))

    def init_ui(self):
        list_obj_ruangan = []
        self.add_ruangan()

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        # Base vertical layout
        v_layout = QtWidgets.QVBoxLayout(widget)

        # Set space between widgets
        v_layout.setSpacing(20)
        v_layout.addStretch(5)

        # Set margin
        v_layout.setContentsMargins(20, 20, 20, 20)

        # Input Container
        input_container = QtWidgets.QHBoxLayout()
        v_layout.addLayout(input_container)
        input_container.addStretch()

        input_grid = QtWidgets.QGridLayout()
        input_container.addLayout(input_grid)

        # Circuit Breaker Name
        entry_label = QtWidgets.QLabel("Enter circuit breaker name:")
        entry_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 17px;
        """
        )
        input_grid.addWidget(entry_label, 0, 0)

        # Text Area
        self.textInput = QtWidgets.QLineEdit()
        self.textInput.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 17px;
            height: 33px;
            border: 2px solid #00AE90;
            border-radius: 4%;
            padding: 3px 10px;
        """
        )
        self.textInput.setFixedWidth(300)
        input_grid.addWidget(self.textInput, 0, 1)

        # Threshold
        threshold_label = QtWidgets.QLabel("Threshold:")
        threshold_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 17px;
        """
        )
        input_grid.addWidget(threshold_label, 1, 0)

        # Threshold Text Area
        self.thresholdInput = QtWidgets.QLineEdit()
        self.thresholdInput.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 17px;
            height: 33px;
            border: 2px solid #00AE90;
            border-radius: 4%;
            padding: 3px 10px;
        """
        )
        self.thresholdInput.setFixedWidth(300)
        input_grid.addWidget(self.thresholdInput, 1, 1)

        input_container.addStretch()

        v_layout.addStretch(2)

        # Room Layout: room label + tickbox layout
        room_layout = QtWidgets.QVBoxLayout()
        v_layout.addLayout(room_layout)

        # Room Label
        room_label_layout = QtWidgets.QHBoxLayout()
        room_label_layout.addStretch()

        room_layout.addLayout(room_label_layout)
        room_label = QtWidgets.QLabel("Daftar Ruangan:")
        room_label.setStyleSheet("color: #FFFFFF;")
        room_label_layout.addWidget(room_label)

        room_label_layout.addStretch()

        # Tickbox Layout
        tickbox_container = QtWidgets.QHBoxLayout()
        room_layout.addLayout(tickbox_container)
        tickbox_container.addStretch()

        tickbox_layout = QtWidgets.QGridLayout()
        tickbox_container.addLayout(tickbox_layout)

        # Add multiple tickboxes here
        num_checkboxes = len(
            self.distinct_room_name
        )  # Number of Circuit Breaker (Can be Modified)
        tickboxes = []
        checkbox_values = [False] * num_checkboxes

        def update_checkbox_val(idx, state):
            checkbox_values[idx] = state == 2

        i = 0
        for ele in self.distinct_room_name:
            # Create a new checkbox
            checkbox = QtWidgets.QCheckBox(ele)
            tickboxes.append(checkbox)

            # Connect the stateChanged signal
            checkbox.stateChanged.connect(
                lambda state, idx=i: update_checkbox_val(idx, state)
            )

            # Calculate the row and column for the tickbox
            row = i // 3
            col = i % 3

            # Add the checkbox to the layout
            tickbox_layout.addWidget(checkbox, row, col)
            i += 1

        tickbox_container.addStretch()

        v_layout.addStretch(1)

        # Button Layout (Next and Finish)
        button_layout = QtWidgets.QHBoxLayout()
        v_layout.addLayout(button_layout)
        button_layout.addStretch()
        next_button = UtilityButton("Next", lambda: on_next_button_clicked())
        next_button.setMinimumSize(90, 90)
        next_button.setStyleSheet(
            """
            UtilityButton {
                color: #00AE90;
                border: 2px solid #00AE90;
                border-radius: 25%;
                font-size: 18px;
            }
            UtilityButton:hover {
                background-color: #00AE90;
                color: #0B2447;
            }
        """
        )
        button_layout.addWidget(next_button)

        def on_next_button_clicked():
            # Clear Text Input
            text = self.textInput.text()
            self.textInput.clear()

            threshold_val = self.thresholdInput.text()
            self.thresholdInput.clear()

            # Validate Threshold Value
            if threshold_val.isdigit() and text != "":
                any_checked = False

                ticked_name = []
                # Tickbox
                for tickbox in tickboxes:
                    if tickbox.isChecked():
                        any_checked = True
                        ticked_name.append(tickbox.text())
                        tickbox.setEnabled(False)
                        tickbox.setStyleSheet(
                            "QCheckBox::indicator {background-color:black; border-radius: 5%}"
                        )

                if any_checked:
                    threshold_val = int(threshold_val)

                    # Add to circuit breaker info
                    self.circuit_breaker_info.append([text, ticked_name, threshold_val])

                    # Insert perangkat listrik into a list
                    for ruangan_name in ticked_name:
                        list_p_listrik = []
                        for pl in self.list_perangkat_listrik:
                            if ruangan_name == pl.get_data_perangkat_listrik()[6]:
                                list_p_listrik.append(pl)

                        ruangan = Ruangan(
                            self.id_ruangan,
                            ruangan_name,
                            list_p_listrik,
                            True,
                            text,
                            threshold_val,
                        )

                        # Append to list_ruangan
                        temp_list_room_name = []
                        for room in self.list_ruangan:
                            temp_list_room_name.append(room.get_ruangan_name())

                        if not ruangan.get_ruangan_name() in temp_list_room_name:
                            self.list_ruangan.append(ruangan)
                            self.id_ruangan += 1
                            self.list_ruangan_updated.emit(self.list_ruangan)
                        else:
                            i = 0
                            for room in self.list_ruangan:
                                if (
                                    room.get_ruangan_name()
                                    == ruangan.get_ruangan_name()
                                ):
                                    break
                                i += 1
                            temp_list = self.list_ruangan[
                                i
                            ].get_list_perangkat_listrik()
                            for ele in list_p_listrik:
                                temp_list.append(ele)
                            self.list_ruangan[i].set_list_perangkat_listrik(temp_list)
                            print(self.list_ruangan[i].get_list_perangkat_listrik())
                            self.list_ruangan_updated.emit(self.list_ruangan)

                for tickbox in tickboxes:
                    if tickbox.isChecked():
                        tickbox.setChecked(False)

            else:
                # Untick the check box
                for tickbox in tickboxes:
                    if tickbox.isChecked():
                        tickbox.setChecked(False)

                msg = QtWidgets.QMessageBox()
                msg.setText("Input Invalid!")
                msg.setInformativeText("Please try to input the correct value!")
                msg.setWindowTitle("Error Message")
                msg.exec_()

        # next_button.clicked.connect(on_next_button_clicked)

        button_layout.addStretch()
        finish_button = UtilityButton("Finish", lambda: on_finish_button_clicked())
        finish_button.setMinimumSize(90, 90)
        finish_button.setStyleSheet(
            """
            UtilityButton {
                background-color: #00AE90;
                color: #0B2447;
                border: 2px solid #00AE90;
                border-radius: 25%;
                font-size: 18px;
            }
            UtilityButton:hover {
                background-color: #0B2447;
                color: #00AE90;
            }
        """
        )
        button_layout.addWidget(finish_button)
        button_layout.addStretch()

        def on_finish_button_clicked():
            text = self.textInput.text()
            threshold_val = self.thresholdInput.text()

            # Validate Threshold Value
            if threshold_val.isdigit() and text != "":
                any_checked = False

                ticked_name = []
                # Tickbox
                for tickbox in tickboxes:
                    if tickbox.isChecked():
                        any_checked = True
                        ticked_name.append(tickbox.text())
                        tickbox.setStyleSheet(
                            "QCheckBox::indicator {background-color:black; border-radius: 5%}"
                        )

                if any_checked:
                    threshold_val = int(threshold_val)

                    # Add to circuit breaker info
                    self.circuit_breaker_info.append([text, ticked_name, threshold_val])

                    # Insert perangkat listrik into a list
                    for ruangan_name in ticked_name:
                        list_p_listrik = []
                        for pl in self.list_perangkat_listrik:
                            if ruangan_name == pl.get_data_perangkat_listrik()[6]:
                                list_p_listrik.append(pl)

                        ruangan = Ruangan(
                            self.id_ruangan,
                            ruangan_name,
                            list_p_listrik,
                            True,
                            text,
                            threshold_val,
                        )

                        # Append to list_ruangan
                        temp_list_room_name = []
                        for room in self.list_ruangan:
                            temp_list_room_name.append(room.get_ruangan_name())

                        if not ruangan.get_ruangan_name() in temp_list_room_name:
                            self.list_ruangan.append(ruangan)
                            self.id_ruangan += 1
                            self.list_ruangan_updated.emit(self.list_ruangan)
                        else:
                            i = 0
                            for room in self.list_ruangan:
                                if (
                                    room.get_ruangan_name()
                                    == ruangan.get_ruangan_name()
                                ):
                                    break
                                i += 1
                            temp_list = self.list_ruangan[
                                i
                            ].get_list_perangkat_listrik()
                            for ele in list_p_listrik:
                                temp_list.append(ele)
                            self.list_ruangan[i].set_list_perangkat_listrik(temp_list)
                            print(self.list_ruangan[i].get_list_perangkat_listrik())
                            self.list_ruangan_updated.emit(self.list_ruangan)

                            for tickbox in tickboxes:
                                if tickbox.isChecked():
                                    tickbox.setChecked(False)
                self.goto("simulator")

            else:
                msg = QtWidgets.QMessageBox()
                msg.setText("Input Invalid!")
                msg.setInformativeText("Please try to input the correct value!")
                msg.setWindowTitle("Error Message")
                msg.exec_()
                self.list_ruangan_updated.emit(self.list_ruangan)
                self.goto("houseframe")

        # finish_button.clicked.connect(on_finish_button_clicked)

        v_layout.addStretch(2)

        # BackButton Layout
        backbutton_layout = QtWidgets.QHBoxLayout()
        v_layout.addLayout(backbutton_layout)
        backbutton_layout.addStretch()
        back_button = UtilityButton("Back", lambda: on_back_button_clicked())
        backbutton_layout.addWidget(back_button)

        def on_back_button_clicked():
            self.goto("datainputv2")

        # back_button.clicked.connect(on_back_button_clicked)

        v_layout.addStretch(1)

    def update_list_perangkat_listrik(self, new_list):
        self.list_perangkat_listrik = new_list
        self.init_ui()

    def add_ruangan(self):
        for perangkat in self.list_perangkat_listrik:
            self.distinct_pl.add(perangkat)
            self.distinct_room_name.add(perangkat.get_data_perangkat_listrik()[6])
