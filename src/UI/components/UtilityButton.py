from components.Button import BaseButton


class UtilityButton(BaseButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(
            """
            UtilityButton {
                background-color: #0B2447;
                border: 2px solid #576CBC;
                color: #576CBC;
                padding: 8px 16px;
                text-align: center;
                text-decoration: none;
                font-size: 18px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 25%;
            }

            UtilityButton:hover {
                background-color: #576CBC;
                color: #0B2447;
            }
        """
        )
