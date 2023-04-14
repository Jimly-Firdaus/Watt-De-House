import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Watt de house")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(0, 0, 1440, 810)

    # Center the window on the screen
    screen = QDesktopWidget().screenGeometry()
    x = (screen.width() - window.width()) // 2
    y = (screen.height() - window.height()) // 2
    window.move(x, y)

    window.show()
    sys.exit(app.exec_())
