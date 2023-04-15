from components.FeatureButton import FeatureButton
from components.UtilityButton import UtilityButton
from util.PageWindow import PageWindow
from PyQt5 import QtWidgets


class MainFrame(PageWindow):
    def __init__(self):
        super().__init__()
        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #0B2447;")
        self.setWindowTitle("Watt de House")

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        # Base vertical layout
        v_layout = QtWidgets.QVBoxLayout(widget)

        # Exit button section
        h1_layout = QtWidgets.QHBoxLayout()
        h1_layout.addStretch()
        self.exitButton = UtilityButton("Exit", None, self)
        self.exitButton.setMinimumSize(90, 90)
        h1_layout.addWidget(self.exitButton)
        v_layout.addLayout(h1_layout)
        v_layout.addStretch()

        # Estimator & Simulator button section
        h2_layout = QtWidgets.QHBoxLayout()
        v_layout.addLayout(h2_layout)
        h2_layout.addStretch()
        self.a1 = FeatureButton("Estimator", None, self)
        self.a1.setMinimumSize(210, 100)
        h2_layout.addWidget(self.a1)
        h2_layout.addStretch()

        self.a2 = FeatureButton("Simulator", lambda: self.moveToPage("simulator"), self)
        self.a2.setMinimumSize(210, 100)
        h2_layout.addWidget(self.a2)
        h2_layout.addStretch()
        v_layout.addStretch()

        # Help button section
        h3_layout = QtWidgets.QHBoxLayout()
        h3_layout.addStretch()
        self.helpButton = UtilityButton("Help", None, self)
        self.helpButton.setMinimumSize(90, 90)
        h3_layout.addWidget(self.helpButton)
        v_layout.addLayout(h3_layout)

    # Callback fn
    def moveToPage(self, page_name):
        if page_name == "simulator":
            self.goto("simulator")
