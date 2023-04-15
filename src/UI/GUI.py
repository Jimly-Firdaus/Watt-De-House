import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from components.FeatureButton import FeatureButton
from components.UtilityButton import UtilityButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget
from components import TextInputContainer


class MainFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1440, 810)
        self.setStyleSheet(
            """
            background-color: #0B2447;
        """
        )

        # Center the self on the screen
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

        # Create a BaseButton and add it to the layout
        self.name = TextInputContainer.TextInputContainer(
            "Name: ", 50, 50, 490, 50, self
        )
        self.name.set_size(490, 50)
        # a1 = FeatureButton("Estimator", self)
        # a1.set_size(210, 100)
        # a1.set_position(440, 350)

        # a2 = FeatureButton("Simulator", self)
        # a2.set_size(210, 100)
        # a2.set_position(770, 350)

        # exitButton = UtilityButton("Exit", self)
        # exitButton.set_size(90, 90)
        # exitButton.set_position(1300, 30)

        # helpButton = UtilityButton("Help", self)
        # helpButton.set_size(90, 90)
        # helpButton.set_position(1300, 650)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainFrame()

    window.show()
    sys.exit(app.exec_())
