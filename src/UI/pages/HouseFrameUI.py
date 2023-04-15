from components.StepButton import StepButton
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets


class HouseFrame(PageWindow):
    def __init__(self):
        super().__init__()
        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #0B2447;")
        self.setWindowTitle("Watt de House")
        self.circuit_breaker_info = []

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
        entry_label.setStyleSheet("color: #FFFFFF;")
        input_grid.addWidget(entry_label, 0, 0)

        # Text Area
        self.textInput = QtWidgets.QLineEdit()
        self.textInput.setStyleSheet("color: #FFFFFF;")
        self.textInput.setFixedWidth(300)
        input_grid.addWidget(self.textInput, 0, 1)

        # Threshold
        threshold_label = QtWidgets.QLabel("Threshold:")
        threshold_label.setStyleSheet("color: #FFFFFF;")
        input_grid.addWidget(threshold_label, 1, 0)

        # Threshold Text Area
        self.thresholdInput = QtWidgets.QLineEdit()
        self.thresholdInput.setStyleSheet("color: #FFFFFF;")
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
        num_checkboxes = 7  # Number of Circuit Breaker (Can be Modified)
        tickboxes = []
        checkbox_values = [False] * num_checkboxes

        def update_checkbox_val(idx, state):
            checkbox_values[idx] = state == 2

        for i in range(num_checkboxes):
            # Create a new checkbox
            checkbox = QtWidgets.QCheckBox(f"Ruangan {i + 1}")
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

        tickbox_container.addStretch()

        v_layout.addStretch(1)

        # Button Layout (Next and Finish)
        button_layout = QtWidgets.QHBoxLayout()
        v_layout.addLayout(button_layout)
        button_layout.addStretch()
        next_button = StepButton("Next")
        button_layout.addWidget(next_button)

        def on_next_button_clicked():
            # Clear Text Input
            text = self.textInput.text()
            self.textInput.clear()

            threshold_val = self.thresholdInput.text()
            self.thresholdInput.clear()

            # Validate Threshold Value
            if threshold_val.isdigit() and text != "":
                threshold_val = int(threshold_val)
                ticked_name = []

                # Tickbox
                for tickbox in tickboxes:
                    if tickbox.isChecked():
                        ticked_name.append(tickbox.text())
                        tickbox.setEnabled(False)
                        tickbox.setStyleSheet(
                            "QCheckBox::indicator {background-color:black; border-radius: 5%}"
                        )

                # Add to circuit breaker info
                self.circuit_breaker_info.append([text, ticked_name, threshold_val])
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

        next_button.clicked.connect(on_next_button_clicked)

        button_layout.addStretch()
        finish_button = StepButton("Finish")
        button_layout.addWidget(finish_button)
        button_layout.addStretch()

        def on_finish_button_clicked():
            if not self.circuit_breaker_info:
                msg = QtWidgets.QMessageBox()
                msg.setText("Empty Input!")
                msg.setInformativeText("Please try to input some values!")
                msg.setWindowTitle("Error Message")
                msg.exec_()
            else:
                self.goto("simulator")

        finish_button.clicked.connect(on_finish_button_clicked)

        v_layout.addStretch(2)

        # BackButton Layout
        backbutton_layout = QtWidgets.QHBoxLayout()
        v_layout.addLayout(backbutton_layout)
        backbutton_layout.addStretch()
        back_button = UtilityButton("Back")
        backbutton_layout.addWidget(back_button)

        v_layout.addStretch(1)
