import sys

sys.path.insert(0, "../../")
from components.FeatureButton import FeatureButton
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from src.ClassFiles.Estimator import Estimator
from src.ClassFiles.DataInput import DataInput1, DataInput2
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from typing import List


class DataInputV2Page(PageWindow):
    list_updated = pyqtSignal(list)

    def __init__(self, list_of_data: List[PerangkatListrik] = []):
        super().__init__()

        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #0B2447;")
        self.setWindowTitle("Data Input V2")
        self.list_of_data = list_of_data

        # create main container
        main_container = QtWidgets.QWidget()
        self.setCentralWidget(main_container)

        main_layout = QtWidgets.QVBoxLayout(main_container)

        # create title container
        title_container = QtWidgets.QWidget()

        title_container.setMaximumHeight(int(self.height() * 0.2))

        title_layout = QtWidgets.QHBoxLayout(title_container)

        title_label = QtWidgets.QLabel("Input Electrical Data")
        title_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 40px;
        """
        )

        title_layout.addStretch()
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

        self.room_input = QtWidgets.QLineEdit()
        self.room_input.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
            height: 33px;
            border: 2px solid #00AE90;
            border-radius: 4%;
            padding: 3px 10px;
        """
        )
        input_layout.addWidget(self.room_input, 4, 1)

        # duration container
        duration_label = QtWidgets.QLabel("Duration: ")
        duration_label.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
        """
        )
        input_layout.addWidget(duration_label, 5, 0)

        self.duration_input = QtWidgets.QLineEdit()
        self.duration_input.setStyleSheet(
            """
            color: #FEFAE0;
            font-size: 19px;
            height: 33px;
            border: 2px solid #00AE90;
            border-radius: 4%;
            padding: 3px 10px;
        """
        )
        input_layout.addWidget(self.duration_input, 5, 1)
        input_container.addStretch()

        # btn container
        btn_container = QtWidgets.QWidget()

        btn_container.setMaximumHeight(int(self.height() * 0.3))

        btn_layout = QtWidgets.QHBoxLayout(btn_container)

        # next btn
        next_btn = UtilityButton(
            "Next", lambda: self.handle_next_button_clicked(), self
        )
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
        finish_btn = UtilityButton("Finish", self.back_to_estimator, self)
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

        btn_layout.addStretch(3)
        btn_layout.addWidget(next_btn)
        btn_layout.addStretch(1)
        btn_layout.addWidget(finish_btn)
        btn_layout.addStretch(3)

        # back btn container
        back_btn_container = QtWidgets.QWidget()
        back_btn_container.setMaximumHeight(int(self.height() * 0.2))
        back_btn_layout = QtWidgets.QHBoxLayout(back_btn_container)
        self.back_btn = UtilityButton("Back", lambda: self.back_to_estimator(), self)
        self.back_btn.setMinimumSize(90, 90)
        back_btn_layout.addStretch()
        back_btn_layout.addWidget(self.back_btn, alignment=QtCore.Qt.AlignBottom)

        main_layout.addWidget(title_container)
        main_layout.addLayout(input_container)
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
            self.list_updated.emit(self.list_of_data)
            self.name_input.clear()
            self.power_spinbox.clear()
            self.voltage_spinbox.clear()
            self.current_spinbox.clear()
            self.room_input.clear()
            self.duration_input.clear()
        except Exception as e:
            print(e)
        print("Total length: " + str(len(self.list_of_data)))


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
