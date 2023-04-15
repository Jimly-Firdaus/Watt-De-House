from components.BaseButton import BaseButton


class StepButton(BaseButton):
    def __init__(self, text, on_click_callback=None, parent=None):
        super().__init__(text, on_click_callback, parent)
        self.setStyleSheet(
            """
            StepButton {
                background-color: #84ACB9;
                border: 2px solid #A5D7E8;
                color: #0B2447;
                padding: 8px 12px;
                text-align: center;
                text-decoration: none;
                font-size: 15px;
                margin: 4px 2px;
                cursor: pointer;
                width: 50px;
                border-radius: 3%;
            }

            StepButton:hover {
                background-color: #0B2447;
                color: #A5D7E8;
            }

        """
        )
