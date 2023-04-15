import sys
from components.FeatureButton import FeatureButton
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from src.ClassFiles.Estimator import Estimator
from src.ClassFiles.DataInput import DataInput1, DataInput2
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from typing import List


class DataInputV2Page(PageWindow):
    def __init__(self, list_of_data: List[PerangkatListrik]):
        super().__init__()

        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #FFFFFF;")
        self.setWindowTitle("Data Input V2")
        self.list_of_data = list_of_data

        # create main container
        main_container = QtWidgets.QWidget()
        self.setCentralWidget(main_container)

        main_layout = QtWidgets.QVBoxLayout(main_container)

        # create title container
        title_container = QtWidgets.QWidget()

        title_container.setMaximumHeight(int(self.height() * 0.1))

        title_layout = QtWidgets.QHBoxLayout(title_container)

        title_label = QtWidgets.QLabel("Input Electrical Device Data Second Version")

        font = QtGui.QFont("Courier New", 20, weight=QtGui.QFont.Bold)

        title_label.setFont(font)

        title_layout.addWidget(title_label)

        # input container
        input_container = QtWidgets.QWidget()

        input_layout = QtWidgets.QVBoxLayout(input_container)

        # name container
        name_container = QtWidgets.QWidget()

        name_container.setMaximumHeight(int(0.1 * input_container.height()))

        name_layout = QtWidgets.QHBoxLayout(name_container)

        name_label = QtWidgets.QLabel("Name    : ")

        self.name_input = QtWidgets.QLineEdit()

        # Set placeholder text to indicate required input
        self.name_input.setPlaceholderText("Required*")

        name_layout.addStretch()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)
        name_layout.addStretch()

        # power container
        power_container = QtWidgets.QWidget()

        power_container.setMaximumHeight(int(0.1 * input_container.height()))

        power_layout = QtWidgets.QHBoxLayout(power_container)

        power_label = QtWidgets.QLabel("Power   : ")

        self.power_spinbox = QtWidgets.QDoubleSpinBox()
        self.power_spinbox.setRange(0, 100)
        self.power_spinbox.setSingleStep(0.1)
        # self.power_spinbox.setValue(50)
        self.power_spinbox.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )

        power_layout.addStretch()
        power_layout.addWidget(power_label)
        power_layout.addWidget(self.power_spinbox)
        power_layout.addStretch()

        # voltage container
        voltage_container = QtWidgets.QWidget()

        voltage_container.setMaximumHeight(int(0.1 * input_container.height()))

        voltage_layout = QtWidgets.QHBoxLayout(voltage_container)

        voltage_label = QtWidgets.QLabel("Voltage : ")

        self.voltage_spinbox = QtWidgets.QDoubleSpinBox()
        self.voltage_spinbox.setRange(0, 100)
        self.voltage_spinbox.setSingleStep(0.1)
        # self.voltage_spinbox.setValue(50)
        self.voltage_spinbox.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )

        voltage_layout.addStretch()
        voltage_layout.addWidget(voltage_label)
        voltage_layout.addWidget(self.voltage_spinbox)
        voltage_layout.addStretch()

        # current container
        current_container = QtWidgets.QWidget()

        current_container.setMaximumHeight(int(0.1 * input_container.height()))

        current_layout = QtWidgets.QHBoxLayout(current_container)

        current_label = QtWidgets.QLabel("Current : ")

        self.current_spinbox = QtWidgets.QDoubleSpinBox()
        self.current_spinbox.setRange(0, 100)
        self.current_spinbox.setSingleStep(0.1)
        # self.current_spinbox.setValue(50)
        self.current_spinbox.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )

        current_layout.addStretch()
        current_layout.addWidget(current_label)
        current_layout.addWidget(self.current_spinbox)
        current_layout.addStretch()

        # room container
        room_container = QtWidgets.QWidget()

        room_container.setMaximumHeight(int(0.1 * input_container.height()))

        room_layout = QtWidgets.QHBoxLayout(room_container)

        room_label = QtWidgets.QLabel("Room    : ")

        self.room_input = QtWidgets.QLineEdit()

        # Set placeholder text to indicate required input
        self.room_input.setPlaceholderText("Required*")

        room_layout.addStretch()
        room_layout.addWidget(room_label)
        room_layout.addWidget(self.room_input)
        room_layout.addStretch()

        # duration container
        duration_container = QtWidgets.QWidget()

        duration_container.setMaximumHeight(int(0.1 * input_container.height()))

        duration_layout = QtWidgets.QHBoxLayout(duration_container)

        duration_label = QtWidgets.QLabel("Duration: ")

        self.duration_input = QtWidgets.QLineEdit()

        self.duration_input.setPlaceholderText("0.00")

        validator = QtGui.QDoubleValidator(decimals=2)
        validator_greater_equal0 = PositiveNumberValidator()

        self.duration_input.setValidator(validator)
        self.duration_input.setValidator(validator_greater_equal0)

        duration_layout.addStretch()
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(self.duration_input)
        duration_layout.addStretch()

        input_layout.addWidget(name_container)
        input_layout.addWidget(power_container)
        input_layout.addWidget(voltage_container)
        input_layout.addWidget(current_container)
        input_layout.addWidget(room_container)
        input_layout.addWidget(duration_container)

        # btn container
        btn_container = QtWidgets.QWidget()

        btn_container.setMaximumHeight(int(self.height() * 0.3))

        btn_layout = QtWidgets.QHBoxLayout(btn_container)

        # next btn
        next_btn = UtilityButton(
            "Next", lambda: self.handle_next_button_clicked(), self
        )
        next_btn.setMinimumSize(90, 90)
        # next_btn.clicked.connect(self.handle_next_button_clicked)

        # finish btn
        finish_btn = UtilityButton("Finish", None, self)
        finish_btn.setMinimumSize(90, 90)

        btn_layout.addStretch()
        btn_layout.addWidget(next_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(finish_btn)
        btn_layout.addStretch()

        # back btn container
        back_btn_container = QtWidgets.QWidget()
        back_btn_container.setMaximumHeight(int(self.height() * 0.2))
        back_btn_layout = QtWidgets.QHBoxLayout(back_btn_container)
        self.back_btn = UtilityButton("Back", lambda: self.back_to_estimator(), self)
        self.back_btn.setMinimumSize(90, 90)
        back_btn_layout.addStretch()
        back_btn_layout.addWidget(self.back_btn, alignment=QtCore.Qt.AlignBottom)

        main_layout.addWidget(title_container)
        main_layout.addWidget(input_container)
        main_layout.addWidget(btn_container)
        main_layout.addWidget(back_btn_container)

    def back_to_estimator(self):
        self.goto("estimator")

    def handle_next_button_clicked(self):
        print(self.name_input.text())
        print(self.power_spinbox.value())
        print(self.voltage_spinbox.value())
        print(self.current_spinbox.value())
        print(self.room_input.text())
        print(self.duration_input.text())
        try:
            duration = self.duration_input.text()
            if not duration:
                duration = float(0)
            else:
                duration = float(self.duration_input.text())
            export_data = DataInput2(
                self.name_input.text(),
                self.power_spinbox.value(),
                self.voltage_spinbox.value(),
                self.current_spinbox.value(),
                self.room_input.text(),
                duration,
            )
            self.list_of_data.append(export_data.create_p_listrik())
            self.name_input.clear()
            self.power_spinbox.clear()
            self.voltage_spinbox.clear()
            self.current_spinbox.clear()
            self.room_input.clear()
            self.duration_input.clear()
        except Exception as e:
            print(e)
        print(self.list_of_data)


class PositiveNumberValidator(QtGui.QDoubleValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setBottom(0)

    def validate(self, input_str, pos):
        result, input_str, pos = super().validate(input_str, pos)
        if input_str == "":
            return (QtGui.QDoubleValidator.Intermediate, input_str, pos)
        else:
            return (result, input_str, pos)
