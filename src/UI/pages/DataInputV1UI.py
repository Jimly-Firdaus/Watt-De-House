import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
from components.FeatureButton import FeatureButton
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtCore, QtGui


class DataInputV1Page(PageWindow):
    def __init__(self,):
        super().__init__()

        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet(
            """
            background-color: #0B2447;
            
            """
        )
        self.setWindowTitle("Data Input V2")

        # create main container
        main_container = QtWidgets.QWidget()
        self.setCentralWidget(main_container)

        main_layout = QtWidgets.QVBoxLayout(main_container)

        # create title container
        title_container = QtWidgets.QWidget()

        title_container.setMaximumHeight(int(self.height() * 0.1))

        title_layout = QtWidgets.QHBoxLayout(title_container)

        title_label = QtWidgets.QLabel("Input Electrical Device Data First Version")

        font = QtGui.QFont("Courier New", 20, weight=QtGui.QFont.Bold)

        title_label.setFont(font)

        title_layout.addWidget(title_label)

        # input container
        input_container = QtWidgets.QWidget()

        input_layout = QtWidgets.QVBoxLayout(input_container)

        # name container
        name_container = QtWidgets.QWidget()

        name_container.setMaximumHeight(int(0.2 * input_container.height()))

        name_layout = QtWidgets.QHBoxLayout(name_container)

        name_label = QtWidgets.QLabel("Name: ")

        name_input = QtWidgets.QLineEdit()

        name_layout.addStretch()
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_input)
        name_layout.addStretch()

        # power container
        power_container = QtWidgets.QWidget()

        power_container.setMaximumHeight(int(0.2 * input_container.height()))

        power_layout = QtWidgets.QHBoxLayout(power_container)

        power_label = QtWidgets.QLabel("Power: ")

        power_spinbox = QtWidgets.QSpinBox()
        power_spinbox.setMinimum(0)
        power_spinbox.setMaximum(100)
        power_spinbox.setStyleSheet(
            """
            QSpinBox {
                color: #576CBC;
                border: 2px solid #19376D; 
                height: 40px;
            }
        """
        )

        # power_spinbox.setValue(50)
        power_spinbox.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )

        power_layout.addStretch()
        power_layout.addWidget(power_label)
        power_layout.addWidget(power_spinbox)
        power_layout.addStretch()

        # voltage container
        voltage_container = QtWidgets.QWidget()

        voltage_container.setMaximumHeight(int(0.2 * input_container.height()))

        voltage_layout = QtWidgets.QHBoxLayout(voltage_container)

        voltage_label = QtWidgets.QLabel("Voltage: ")

        voltage_spinbox = QtWidgets.QSpinBox()
        voltage_spinbox.setMinimum(0)
        voltage_spinbox.setMaximum(100)
        # voltage_spinbox.setValue(50)
        voltage_spinbox.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )

        voltage_layout.addStretch()
        voltage_layout.addWidget(voltage_label)
        voltage_layout.addWidget(voltage_spinbox)
        voltage_layout.addStretch()

        # current container
        current_container = QtWidgets.QWidget()

        current_container.setMaximumHeight(int(0.2 * input_container.height()))

        current_layout = QtWidgets.QHBoxLayout(current_container)

        current_label = QtWidgets.QLabel("Current: ")

        current_spinbox = QtWidgets.QSpinBox()
        current_spinbox.setMinimum(0)
        current_spinbox.setMaximum(100)
        # current_spinbox.setValue(50)
        current_spinbox.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )

        current_layout.addStretch()
        current_layout.addWidget(current_label)
        current_layout.addWidget(current_spinbox)
        current_layout.addStretch()

        # duration container
        room_name_container = QtWidgets.QWidget()

        room_name_container.setMaximumHeight(int(0.2 * input_container.height()))

        room_name_layout = QtWidgets.QHBoxLayout(room_name_container)

        room_name_label = QtWidgets.QLabel("Room Name: ")

        room_name_input = QtWidgets.QLineEdit()

        room_name_layout.addStretch()
        room_name_layout.addWidget(room_name_label)
        room_name_layout.addWidget(room_name_input)
        room_name_layout.addStretch()

        input_layout.addWidget(name_container)
        input_layout.addWidget(power_container)
        input_layout.addWidget(voltage_container)
        input_layout.addWidget(current_container)
        input_layout.addWidget(room_name_container)

        # btn container
        btn_container = QtWidgets.QWidget()

        btn_container.setMaximumHeight(int(self.height() * 0.3))

        btn_layout = QtWidgets.QHBoxLayout(btn_container)

        # next btn
        next_btn = UtilityButton("Next", None, self)
        next_btn.setMinimumSize(90, 90)

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
