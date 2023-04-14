from PyQt5.QtWidgets import QPushButton


class BaseButton(QPushButton):
    def __init__(self, label, parent=None):
        super().__init__(label, parent)
        self.clicked.connect(self.on_click)

        style_sheet = """
            BaseButton {
                background-color: red;
                color: white;
                border: none;
                font-size: 18px;
            }
            BaseButton:hover {
                background-color: blue;
            }
            BaseButton:pressed {
                background-color: green;
            }
        """

        self.set_style(style_sheet)

    def on_click(self):
        # Callback function here
        self.setText("Clicked!")

    def set_size(self, width, height):
        self.setFixedSize(width, height)

    def set_position(self, x, y):
        self.move(x, y)

    def set_style(self, style_sheet):
        self.setStyleSheet(style_sheet)
