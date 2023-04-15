import sys

sys.path.insert(0, "../")
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from components.BaseCard import BaseCard
from pages.MainPageUI import MainFrame
from pages.SimulatorUI import SimulatorPage
from pages.EstimatorUI import EstimatorPage
from pages.DataInputV1UI import DataInputV1Page
from pages.DataInputV2UI import DataInputV2Page
from pages.HelpUI import HelpPage
from pages.HouseFrameUI import HouseFrame
from src.ClassFiles.PerangkatListrik import PerangkatListrik
from src.ClassFiles.Ruangan import Ruangan
from src.ClassFiles.Database import Database
from composables.Utility import Util


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 1440, 810)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.db = Database("watt_de_house.db")
        # Create table incase doesnot exist
        self.db.create_table(
            "perangkat_listrik",
            {
                "id": "INTEGER PRIMARY KEY",
                "status": "TEXT",
                "nama": "TEXT",
                "daya": "REAL",
                "arus": "REAL",
                "tegangan": "REAL",
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

        # Fetch all data from database
        list_ruangan = Util.get_all_ruangan(self.db)
        list_perangkat_listrik = []

        # Center the opened window
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

        # Pages here
        self.m_pages = {}

        # Register page here
        self.register(MainFrame(), "main")
        self.register(HelpPage(), "help")
        self.register(HouseFrame(list_perangkat_listrik, list_ruangan), "houseframe")
        self.register(SimulatorPage(list_ruangan), "simulator")
        self.register(EstimatorPage(list_perangkat_listrik), "estimator")
        self.register(DataInputV1Page(list_perangkat_listrik), "datainputv1")
        self.register(DataInputV2Page(list_perangkat_listrik), "datainputv2")

        data_input_v1_page = self.m_pages["datainputv1"]
        data_input_v2_page = self.m_pages["datainputv2"]
        house_frame = self.m_pages["houseframe"]
        data_input_v1_page.list_updated.connect(
            house_frame.update_list_perangkat_listrik
        )
        data_input_v2_page.list_updated.connect(
            house_frame.update_list_perangkat_listrik
        )

        # Defaults to main
        self.goto("main")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, QWidget):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
