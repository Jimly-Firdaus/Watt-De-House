import sys

sys.path.insert(0, "../../")
from PyQt5.QtCore import Qt
from UI.components.FeatureButton import FeatureButton
from UI.components.UtilityButton import UtilityButton
from UI.util.PageWindow import PageWindow
from PyQt5 import QtWidgets
from UI.components.UtilityButton import UtilityButton


class HelpPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #0B2447;")
        self.setWindowTitle("Watt de House")

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        self.label = QtWidgets.QLabel("hello world", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: red; font-size: 30px;")

        self.BackButton = UtilityButton("Back", lambda: self.back_to_main(), self)
        self.BackButton.setMinimumSize(90, 90)
        self.BackButton.clicked.connect(self.back_to_main)

        v_layout = QtWidgets.QVBoxLayout(widget)

        h1_layout = QtWidgets.QHBoxLayout()
        h1_layout.addStretch()
        h1_layout.addWidget(self.BackButton)

        v_layout.addStretch(5)
        h2_layout = QtWidgets.QHBoxLayout()
        h2_layout.addStretch()

        h2_layout.addWidget(self.label)
        h2_layout.addStretch()
        v_layout.addLayout(h2_layout)

        # Create the button and set its properties

        v_layout.addStretch(5)
        v_layout.addLayout(h1_layout)

        self.setLayout(v_layout)

    def back_to_main(self):
        self.goto("main")
