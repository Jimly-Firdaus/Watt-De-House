from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget


class BaseCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.button_layout = QHBoxLayout()

    def add_text(self, text, alignment="left"):
        label = QLabel(text)
        label.setWordWrap(True)
        if alignment == "left":
            self.layout.addWidget(label, alignment=Qt.AlignLeft)
        elif alignment == "center":
            self.layout.addWidget(label, alignment=Qt.AlignHCenter)
        elif alignment == "right":
            self.layout.addWidget(label, alignment=Qt.AlignRight)

    def add_button(self, text):
        button = QPushButton(text)
        self.button_layout.addWidget(button)

    def set_style(self, style_sheet):
        self.setStyleSheet(style_sheet)

    def set_size(self, width, height):
        self.setFixedSize(width, height)

    def finalize(self):
        self.layout.addLayout(self.button_layout)

    # How to use (uncomment this then copy to main to test)
    # card = BaseCard(window)
    # card.set_size(700, 700)
    # card.add_text("This is some left-aligned text.", alignment='left')
    # card.add_text("This is some centered text.", alignment='center')
    # card.add_text("This is some text.")
    # card.add_button("Button 1")
    # card.add_button("Button 2")
    # card.set_style("""
    #     Card {
    #         background-color: lightgray;
    #         padding: 10px;
    #     }
    #     QLabel {
    #         color: blue;
    #     }
    #     QPushButton {
    #         background-color: red;
    #         color: white;
    #     }
    # """)
    # card.finalize()
