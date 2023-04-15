import sys
from components.FeatureButton import FeatureButton
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from src.ClassFiles.Estimator import Estimator
from src.ClassFiles.DataInput import DataInput1, DataInput2
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from typing import List


class EstimatorPage(PageWindow):
    def __init__(self, list_of_data: List[PerangkatListrik]):
        super().__init__()
        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #FFFFFF;")
        self.setWindowTitle("Estimator")
        self.list_of_data = list_of_data

        font = QtGui.QFont("Courier New", 20, weight=QtGui.QFont.Bold)

        result_font = QtGui.QFont("Courier New", 15, weight=QtGui.QFont.Bold)

        # create main container
        main_container = QtWidgets.QWidget()
        self.setCentralWidget(main_container)

        main_layout = QtWidgets.QVBoxLayout(main_container)

        # title container
        title_container = QtWidgets.QWidget()

        title_layout = QtWidgets.QHBoxLayout(title_container)

        self.title_label = QtWidgets.QLabel("Electrical Used Price Estimator")

        self.title_label.setFont(font)

        title_layout.addStretch()
        title_layout.addWidget(self.title_label, alignment=QtCore.Qt.AlignBottom)
        title_layout.addStretch()

        # create button to dpl 2
        btn_container = QtWidgets.QWidget()
        btn_layout = QtWidgets.QHBoxLayout(btn_container)
        self.btn_to_dpl2 = UtilityButton(
            "Please Press Here to Include Data", self.go_to_input_data_v2, self
        )
        self.btn_to_dpl2.setMinimumSize(90, 90)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_to_dpl2)
        btn_layout.addStretch()

        # create go button
        # go_btn_container = QtWidgets.QWidget()
        # go_btn_layout = QtWidgets.QHBoxLayout(go_btn_container)
        # self.go_btn = UtilityButton("Calculate Estimation", None, self)
        # self.go_btn.setMinimumSize(90, 90)
        # go_btn_layout.addStretch()
        # go_btn_layout.addWidget(self.go_btn)
        # go_btn_layout.addStretch()

        # create price defined container
        price_container = QtWidgets.QWidget()

        price_container.setMaximumHeight(int(0.1 * main_container.height()))

        price_layout = QtWidgets.QHBoxLayout(price_container)

        price_label = QtWidgets.QLabel("price: ")

        self.price_input = QtWidgets.QLineEdit()

        # Set placeholder text to indicate required input
        self.price_input.setPlaceholderText("605")

        price_layout.addStretch()
        price_layout.addWidget(price_label)
        price_layout.addWidget(self.price_input)
        price_layout.addStretch()

        # create result container
        result_container = QtWidgets.QWidget()
        result_layout = QtWidgets.QHBoxLayout(result_container)

        result_str = self.get_estimator()
        self.result_label = QtWidgets.QLabel(result_str)
        self.result_label.setFont(result_font)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_label)
        timer.start(1000)

        result_layout.addStretch()
        result_layout.addWidget(self.result_label)
        result_layout.addStretch()

        # create back button
        back_btn_container = QtWidgets.QWidget()
        back_btn_container.setMaximumHeight(int(self.height() * 0.2))
        back_btn_layout = QtWidgets.QHBoxLayout(back_btn_container)
        self.back_btn = UtilityButton("Back", lambda: self.back_to_main(), self)
        self.back_btn.setMinimumSize(90, 90)
        back_btn_layout.addStretch()
        back_btn_layout.addWidget(self.back_btn, alignment=QtCore.Qt.AlignBottom)

        # main_layout.addWidget(QtWidgets.QLabel("Up"))
        main_layout.addWidget(title_container)
        main_layout.addWidget(btn_container)
        main_layout.addWidget(price_container)
        main_layout.addWidget(result_container)
        main_layout.addWidget(back_btn_container)

    def back_to_main(self):
        self.goto("main")

    def go_to_input_data_v2(self):
        self.goto("inputdatav2")

    def update_label(self):
        update_result_str = self.get_estimator()
        self.result_label.setText(update_result_str)

    def get_estimator(self):
        input_value = self.price_input.text()
        if not input_value:
            input_value = float(605)
        else:
            input_value = float(input_value)
        estimator_obj = Estimator(True, self.list_of_data, input_value)
        estimator_obj.hitung_biaya_listrik()
        return estimator_obj.display_total_biaya()
        # self.setLayout(main_layout)

        # # get the center position of the main container
        # center_pos = main_container.rect().center()

        # create title container
        # title_container = QtWidgets.QWidget()
        # title_layout = QtWidgets.QHBoxLayout(title_container)
        # title_layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        # title_layout.setContentsMargins(0, -50, 0, 0)  # move container up

        # title_label = QtWidgets.QLabel("Hello World!")
        # title_label.setAlignment(QtCore.Qt.AlignCenter)

        # # set font family and size
        # font = QtGui.QFont("Arial", 18)
        # title_label.setFont(font)

        # # add stretchable spaces on both sides of the label
        # title_layout.addStretch()
        # title_layout.addWidget(title_label)
        # title_layout.addStretch()

        # # calculate the position of the title container based on the center position of the main container
        # x = round((main_container.width() - title_container.width()) / 2)
        # y = round(main_container.height() * 0.4)
        # title_container.setGeometry(x, y, title_container.width(), title_container.height())

        # main_layout.addWidget(title_container)
