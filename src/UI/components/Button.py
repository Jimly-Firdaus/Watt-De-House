from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class BaseButton(QPushButton):
    def __init__(self, label, parent=None):
        super().__init__(label, parent)
        self.clicked.connect(self.on_click)

    def on_click(self):
        # Callback function here
        pass

    def set_size(self, width, height):
        self.setFixedSize(width, height)

    def set_position(self, x, y):
        self.move(x, y)

    def set_style(self, style_sheet):
        self.setStyleSheet(style_sheet)
