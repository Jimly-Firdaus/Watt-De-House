from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit


class BaseInput(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set a custom style for the input widget
        self.setStyleSheet(
            """
            BaseInput {
                border: 2px solid blue;
                border-radius: 10px;
                padding: 5px;
            }
            BaseInput:focus {
                border-color: lightblue;
            }
        """
        )

    def keyPressEvent(self, event):
        # Add custom behavior for key presses
        if event.key() == Qt.Key_Return:
            print("Return key pressed!")

        # Call the base class implementation to handle other key presses
        super().keyPressEvent(event)

    def set_style(self, style_sheet):
        current_style = self.styleSheet()
        new_style = current_style + "\n" + style_sheet
        self.setStyleSheet(new_style)

    def set_size(self, width, height):
        self.setFixedSize(width, height)

    def set_position(self, x, y):
        self.move(x, y)

    # How to use (uncomment this then copy to main to test)
    # layout = QVBoxLayout(self)
    # input = BaseInput()
    # style_sheet = """
    #     QLineEdit {
    #         color: red;
    #         font-size: 18px;
    #     }
    # """
    # input.set_style(style_sheet)
    # input.set_size(200, 50)
    # layout.addWidget(input)
