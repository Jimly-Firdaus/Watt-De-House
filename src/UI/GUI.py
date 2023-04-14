import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from components.FeatureButton import FeatureButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            """
            background-color: #0B2447;
        """
        )
        self.resize(1280, 720)
        self.setWindowTitle("Watt de house")
        self.a1 = FeatureButton("Estimator", self)
        self.a1.setGeometry(380, 270, 200, 90)
        self.a2 = FeatureButton("Simulator", self)
        self.a2.setGeometry(700, 270, 200, 90)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
