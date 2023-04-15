from components.BaseButton import BaseButton


class FeatureButton(BaseButton):
    def __init__(self, text, on_click_callback=None, parent=None):
        super().__init__(text, on_click_callback, parent)
        self.setStyleSheet(
            """
            FeatureButton {
                background-color: #A5D7E8;
                border: 2px solid #A5D7E8;
                color: #0B2447;
                padding: 8px 16px;
                text-align: center;
                text-decoration: none;
                font-size: 20px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 7%;
            }

            FeatureButton:hover {
                background-color: #0B2447;
                color: #A5D7E8;
            }

        """
        )
