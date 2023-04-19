import sys
import time

sys.path.insert(0, "../")
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from UI.pages.MainPageUI import MainFrame
from UI.pages.SimulatorUI import SimulatorPage
from UI.pages.EstimatorUI import EstimatorPage
from UI.pages.DataInputV1UI import DataInputV1Page
from UI.pages.DataInputV2UI import DataInputV2Page
from UI.pages.HelpUI import HelpPage
from UI.pages.HouseFrameUI import HouseFrame
from ClassFiles.Database import Database
from UI.composables.Utility import Util


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 1440, 810)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

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

        # Fetch all data from database
        list_ruangan, list_perangkat_listrik = Util.get_all_data(self.db)

        # Center the opened window
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

        # Pages here
        self.m_pages = {}

        list_perangkat_listrik2 = []

        # Register page here
        self.register(MainFrame(list_ruangan, list_perangkat_listrik, self.db), "main")
        self.register(HelpPage(), "help")
        self.register(HouseFrame(list_perangkat_listrik, list_ruangan), "houseframe")
        self.register(SimulatorPage(list_ruangan), "simulator")
        self.register(EstimatorPage(list_perangkat_listrik2), "estimator")
        self.register(DataInputV1Page(list_perangkat_listrik), "datainputv1")
        self.register(DataInputV2Page(list_perangkat_listrik2), "datainputv2")

        data_input_v1_page = self.m_pages["datainputv1"]
        data_input_v2_page = self.m_pages["datainputv2"]
        house_frame = self.m_pages["houseframe"]
        simulator_page = self.m_pages["simulator"]
        main_page = self.m_pages["main"]
        data_input_v1_page.list_updated.connect(
            house_frame.update_list_perangkat_listrik
        )
        data_input_v2_page.list_updated.connect(
            house_frame.update_list_perangkat_listrik
        )
        house_frame.list_ruangan_updated.connect(simulator_page.update_self_list)
        main_page.list_ruangan_updated.connect(simulator_page.update_self_list)
        main_page.list_ruangan_updated.connect(house_frame.update_self_list)
        house_frame.list_ruangan_updated.connect(main_page.update_self_list)
        main_page.reset.connect(house_frame.reset_self_list)

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


def run_app(exit_flag):
    import sys

    app = QApplication(sys.argv)
    window = Window()

    window.show()

    # Run the application event loop until the exit_flag is set
    while not exit_flag.is_set():
        app.processEvents()
        time.sleep(0.1)

    sys.exit()
