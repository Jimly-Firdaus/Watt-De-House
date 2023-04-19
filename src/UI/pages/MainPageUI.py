import sys

sys.path.insert(0, "../../")
from UI.components.FeatureButton import FeatureButton
from UI.components.UtilityButton import UtilityButton
from UI.util.PageWindow import PageWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from UI.composables.Utility import Util
import os
from typing import List
from ClassFiles.Ruangan import Ruangan
from src.ClassFiles.Database import Database


class MainFrame(PageWindow):
    list_ruangan_updated = QtCore.pyqtSignal(list)

    def __init__(self, list_ruangan, list_perangkat_listrik, db):
        super().__init__()
        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #0B2447;")
        self.setWindowTitle("Watt de House")
        self.list_ruangan = list_ruangan
        self.db = db
        self.list_perangkat_listrik = list_perangkat_listrik
        self.init_ui()

    def init_ui(self):
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        # Base vertical layout
        v_layout = QtWidgets.QVBoxLayout(widget)

        # Exit button section
        h1_layout = QtWidgets.QHBoxLayout()
        h1_layout.addStretch()
        self.exitButton = UtilityButton("Exit", lambda: self.move_to_page("exit"), self)
        self.exitButton.setMinimumSize(90, 90)
        h1_layout.addWidget(self.exitButton)
        v_layout.addLayout(h1_layout)
        v_layout.addStretch(5)

        # Feature Label
        ft_label_layout = QtWidgets.QHBoxLayout()
        v_layout.addLayout(ft_label_layout)
        ft_label_layout.addStretch()

        ft_label = QtWidgets.QLabel("FEATURES")
        ft_font = QtGui.QFont("Georgia", 24)
        ft_label.setFont(ft_font)
        ft_label.setStyleSheet("color:#FEFAE0;")
        ft_label_layout.addWidget(ft_label)

        ft_label_layout.addStretch()
        v_layout.addStretch(2)

        # Estimator & Simulator button section
        # Font
        ft_button_font = QtGui.QFont("Georgia", 16)

        # Layout
        h2_layout = QtWidgets.QHBoxLayout()
        v_layout.addLayout(h2_layout)
        h2_layout.addStretch()
        self.a1 = FeatureButton(
            "Estimator", lambda: self.move_to_page("estimator"), self
        )
        self.a1.setFont(ft_button_font)
        self.a1.setMinimumSize(210, 100)
        h2_layout.addWidget(self.a1)
        h2_layout.addStretch()

        self.a2 = FeatureButton(
            "Simulator", lambda: self.move_to_page("simulator"), self
        )
        self.a2.setFont(ft_button_font)
        self.a2.setMinimumSize(210, 100)
        h2_layout.addWidget(self.a2)
        h2_layout.addStretch()
        v_layout.addStretch(5)

        # Help button section
        h3_layout = QtWidgets.QHBoxLayout()
        self.helpButton = UtilityButton("Help", lambda: self.move_to_page("help"), self)
        self.helpButton.setMinimumSize(90, 90)

        self.reset_data_btn = UtilityButton(
            "Reset Database", self.handle_reset_database, self
        )
        self.reset_data_btn.setMinimumSize(90, 90)
        h3_layout.addWidget(self.reset_data_btn)
        h3_layout.addStretch()
        h3_layout.addWidget(self.helpButton)
        v_layout.addLayout(h3_layout)

    # Callback fn
    def move_to_page(self, page_name):
        if page_name == "simulator":
            self.goto("simulator")
        elif page_name == "estimator":
            self.goto("estimator")
        elif page_name == "help":
            self.goto("help")
        elif page_name == "exit":
            Util.store_to_db(self.db, self.list_ruangan)
            sys.exit()

    def update_user_data(self, list_ruangan, list_perangkat_listrik):
        self.list_ruangan = list_ruangan
        self.list_perangkat_listrik = list_perangkat_listrik
        self.init_ui()

    def handle_reset_database(self):
        self.db.close()
        if os.path.exists("watt_de_house.db"):
            os.remove("watt_de_house.db")
            self.db = Database("watt_de_house.db")
            self.modified_state = False
            # Create table incase doesnot exist
            self.db.create_table(
                "perangkat_listrik",
                {
                    "id": "INTEGER PRIMARY KEY",
                    "status": "INTEGER",
                    "nama": "TEXT",
                    "daya": "REAL",
                    "arus": "REAL",
                    "tegangan": "REAL",
                    "nama_ruangan": "TEXT",
                    "durasi": "INTEGER",
                },
            )
            self.db.create_table(
                "ruangan",
                {
                    "id": "INTEGER PRIMARY KEY",
                    "nama_ruangan": "TEXT",
                    "circuit_breaker": "INTEGER",
                    "circuit_breaker_name": "TEXT",
                    "threshold": "REAL",
                },
            )
            self.db.create_table(
                "ruangan_perangkat_listrik",
                {
                    "id_ruangan": "INTEGER",
                    "id_perangkat_listrik": "INTEGER",
                },
            )
            self.list_ruangan = []
            self.list_ruangan, self.list_perangkat_listrik = Util.get_all_data(self.db)
            self.list_ruangan_updated.emit(self.list_ruangan)

    def update_self_list(self, new_list: List[Ruangan]):
        self.list_ruangan = new_list
        self.init_ui()
