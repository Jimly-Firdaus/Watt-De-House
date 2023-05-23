import sys

sys.path.insert(0, "../../")
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
from UI.components.UtilityButton import UtilityButton
from UI.util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtCore
from ClassFiles.DataInput import DataInput1


class DataInputV1Page(PageWindow):
    list_updated = pyqtSignal(list)

    def __init__(
        self,
        data_input_v1_list: list = [],
    ):
        super().__init__()
        self.temp_data = []

        # List of tuple (name, power, voltage, current, room_name)
        self.v1_list = data_input_v1_list

        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet(
            """
            background-color: #0B2447;
            """
        )
        self.setWindowTitle("Data Input V1")
        self.id_perangkat_listrik = len(self.v1_list)

        # create main container
        main_container = QtWidgets.QWidget()
        self.setCentralWidget(main_container)

        main_layout = QtWidgets.QVBoxLayout(main_container)

        # create title container
        title_container = QtWidgets.QWidget()

        title_container.setMaximumHeight(int(self.height() * 0.2))

        title_layout = QtWidgets.QHBoxLayout(title_container)

        title_layout.addStretch()
        title_label = QtWidgets.QLabel("Input Electrical Data")
        title_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 40px;
        """
        )

        title_layout.addWidget(title_label)
        title_layout.addStretch()

        # input container
        input_container = QtWidgets.QHBoxLayout()
        input_container.addStretch()

        input_layout = QtWidgets.QGridLayout()
        input_container.addLayout(input_layout)

        # name container
        name_label = QtWidgets.QLabel("Name: ")
        name_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
        """
        )
        input_layout.addWidget(name_label, 0, 0)

        self.name_input = QtWidgets.QLineEdit()
        self.name_input.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
            height: 33px;
            border: 2px solid #00AE90;
            border-radius: 4%;
            padding: 3px 10px;
        """
        )
        self.name_input.setPlaceholderText("Required")
        input_layout.addWidget(self.name_input, 0, 1)

        # power container
        power_label = QtWidgets.QLabel("Power: ")
        power_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
        """
        )
        input_layout.addWidget(power_label, 1, 0)

        self.power_spinbox = QtWidgets.QSpinBox()
        self.power_spinbox.setMinimum(0)
        self.power_spinbox.setMaximum(200)
        self.power_spinbox.setStyleSheet(
            """
            QSpinBox {
                color: #FEFAE0;
                font-size: 19px;
                height: 33px;
                border: 2px solid #00AE90;
                border-radius: 4%;
                padding: 3px 10px 3px 3px;
            }
        """
        )
        input_layout.addWidget(self.power_spinbox, 1, 1)

        # power_spinbox.setValue(50)
        # self.power_spinbox.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # voltage container
        voltage_label = QtWidgets.QLabel("Voltage: ")
        voltage_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
        """
        )
        input_layout.addWidget(voltage_label, 2, 0)

        self.voltage_spinbox = QtWidgets.QSpinBox()
        self.voltage_spinbox.setMinimum(120)
        self.voltage_spinbox.setMaximum(300)
        # self.voltage_spinbox.setValue(50)
        # self.voltage_spinbox.setSizePolicy(
        #     QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        # )
        self.voltage_spinbox.setStyleSheet(
            """
            QSpinBox {
                color: #FEFAE0;
                font-size: 19px;
                height: 33px;
                border: 2px solid #00AE90;
                border-radius: 4%;
                padding: 3px 10px 3px 3px;
            }
        """
        )
        input_layout.addWidget(self.voltage_spinbox, 2, 1)

        # current container

        current_label = QtWidgets.QLabel("Current: ")
        current_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
        """
        )
        input_layout.addWidget(current_label, 3, 0)

        self.current_spinbox = QtWidgets.QSpinBox()
        self.current_spinbox.setMinimum(0)
        self.current_spinbox.setMaximum(100)
        # self.current_spinbox.setValue(50)
        # self.current_spinbox.setSizePolicy(
        #     QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        # )
        self.current_spinbox.setStyleSheet(
            """
            QSpinBox {
                color: #FEFAE0;
                font-size: 19px;
                height: 33px;
                border: 2px solid #00AE90;
                border-radius: 4%;
                padding: 3px 10px 3px 3px;
            }
        """
        )

        input_layout.addWidget(self.current_spinbox, 3, 1)

        # duration container

        room_name_label = QtWidgets.QLabel("Room Name: ")
        room_name_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
        """
        )
        input_layout.addWidget(room_name_label, 4, 0)

        self.room_name_input = QtWidgets.QLineEdit()
        self.room_name_input.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
            height: 33px;
            border: 2px solid #00AE90;
            border-radius: 4%;
            padding: 3px 10px;
        """
        )
        self.room_name_input.setPlaceholderText("Required")
        input_layout.addWidget(self.room_name_input, 4, 1)

        # btn container
        btn_container = QtWidgets.QWidget()

        btn_container.setMaximumHeight(int(self.height() * 0.3))

        btn_layout = QtWidgets.QHBoxLayout(btn_container)

        # next btn
        next_btn = UtilityButton("Next", lambda: self.next_device(), self)
        next_btn.setMinimumSize(90, 90)
        next_btn.setStyleSheet(
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

        # finish btn
        finish_btn = UtilityButton("Finish", lambda: self.finish_input(), self)
        finish_btn.setMinimumSize(90, 90)
        finish_btn.setStyleSheet(
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

        input_container.addStretch()

        btn_layout.addStretch(3)
        btn_layout.addWidget(next_btn)
        btn_layout.addStretch(1)
        btn_layout.addWidget(finish_btn)
        btn_layout.addStretch(3)

        # back btn container
        back_btn_container = QtWidgets.QWidget()
        back_btn_container.setMaximumHeight(int(self.height() * 0.2))
        back_btn_layout = QtWidgets.QHBoxLayout(back_btn_container)
        self.back_btn = UtilityButton("Back", lambda: self.back_to_simulator(), self)
        self.back_btn.setMinimumSize(90, 90)
        self.reset_btn = UtilityButton(
            "Reset", lambda: self.handle_reset_btn_clicked(), self
        )
        self.error_label = QtWidgets.QLabel("The input you give is incorrect!")
        self.error_label.setStyleSheet(
            """
            color: red;
        """
        )
        self.error_label.setVisible(False)
        self.reset_btn.setMinimumSize(90, 90)
        back_btn_layout.addWidget(self.reset_btn, alignment=QtCore.Qt.AlignBottom)
        back_btn_layout.addStretch()
        back_btn_layout.addWidget(self.error_label)
        back_btn_layout.addStretch()
        back_btn_layout.addWidget(self.back_btn, alignment=QtCore.Qt.AlignBottom)

        main_layout.addWidget(title_container)
        main_layout.addLayout(input_container)
        main_layout.addWidget(btn_container)
        main_layout.addWidget(back_btn_container)

    def add_to_list(self):
        device_name = self.name_input.text()
        device_power = self.power_spinbox.value()
        device_voltage = self.voltage_spinbox.value()
        device_current = self.current_spinbox.value()
        device_room_name = self.room_name_input.text()
        self.id_perangkat_listrik = len(self.v1_list) + 1
        device = DataInput1(
            self.id_perangkat_listrik,
            device_name,
            device_power,
            device_current,
            device_voltage,
            device_room_name,
        )
        self.temp_data.append(device.create_p_listrik())
        self.reset_values()

    def back_to_simulator(self):
        self.reset_values()
        self.error_label.setVisible(False)
        self.goto("simulator")

    def reset_values(self):
        self.name_input.clear()
        self.name_input.setPlaceholderText("Required")
        self.power_spinbox.clear()
        self.power_spinbox.setValue(0)
        self.voltage_spinbox.clear()
        self.voltage_spinbox.setValue(120)
        self.current_spinbox.clear()
        self.current_spinbox.setValue(0)
        self.room_name_input.clear()
        self.room_name_input.setPlaceholderText("Required")

    def next_device(self):
        try:
            self.add_to_list()
            self.error_label.setVisible(False)
        except Exception as e:
            self.error_label.setVisible(True)

    def handle_reset_btn_clicked(self):
        self.reset_values()
        self.error_label.setVisible(False)
        self.temp_data = []

    def finish_input(self):
        try:
            self.add_to_list()
            self.error_label.setVisible(False)
            for data in self.temp_data:
                self.v1_list.append(data)
                self.list_updated.emit(self.v1_list)
            self.temp_data = []
            self.goto("houseframe")
        except Exception as e:
            self.error_label.setVisible(True)
