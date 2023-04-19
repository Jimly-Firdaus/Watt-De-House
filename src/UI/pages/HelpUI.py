import sys

sys.path.insert(0, "../../")
from PyQt5.QtCore import Qt
from UI.components.FeatureButton import FeatureButton
from UI.components.UtilityButton import UtilityButton
from UI.util.PageWindow import PageWindow
from PyQt5 import QtWidgets
from UI.components.UtilityButton import UtilityButton


class HelpPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.setBaseSize(1024, 720)
        self.setSizeIncrement(2, 2)
        self.setStyleSheet("background-color: #0B2447;")
        self.setWindowTitle("Watt de House")

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)

        self.label = QtWidgets.QLabel("HELP", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: #FEFAE0; font-size: 40px; weight: bold; ")

        self.text = QtWidgets.QTextEdit(self)
        self.text.setReadOnly(True)
        self.text.setAlignment(Qt.AlignJustify)
        self.text.setStyleSheet(
            """
            font-size: 24px; 
            color: #FEFAE0; 
            background-color: #0B2447; 
            height: 200px; 
            width: 500px; 
            font-family: Times New Roman;
            border: 5px solid #00AE90;
            """
        )

        text = "FITUR ESTIMATOR \n1. Klik estimator untuk menjalakan fitur estimator \n2. Jika ingin menambahkan data, klik 'Please Press Here To Include Data' \n3. Masukkan data perangkat listrik yang diminta \n4. Jika ingin menambahkan lebih dari 1 perangkat listrik, klik tombol next setelah memasukkan data satu perangkat listrik untuk lanjut memasukkan data perangkat lainnya \n5. Jika data yang dimasukkan sudah merupakan data terakhir, klik finish. \n6. Hasil estimasi biaya akan tertampilkan setelah tombol finish diklik \n\nFITUR SIMULATOR \n1. Klik simulator untuk menjalankan fitur simulator \n2. Jika ingin menambahkan data, klik 'Tambahkan Perangkat Listrik' \n3. Masukkan data perangkat listrik yang diminta \n4. Jika ingin menambahkan lebih dari 1 perangkat listrik, klik tombol next setelah memasukkan data satu perangkat listrik untuk lanjut memasukkan data perangkat lainnya \n5. Jika data yang dimasukkan sudah merupakan data terakhir, klik finish. \n6. Perlu diingat, pada fitur ini, setelah melakukan klik tombol finish, jika ingin menambahkan perangkat listrik lagi, ruangan yang sudah dimasukkan pada input sebelumnya tidak bisa diinput lagi/dimasukkan perangkat listrik baru (Pastikan untuk klik tombol reset sebelum melakukan input data perangkat listrik yang baru) \n7. Fitur simulasi sudah siap digunakan. Klik checkbox pada perangkat listrik yang ingin dinyalakan saat simulasi \n8. Anda dapat melihat status electrical overload pada bagian kiri atas halaman "
        self.text.setText(text)

        self.BackButton = UtilityButton("Back", lambda: self.back_to_main(), self)
        self.BackButton.setMinimumSize(90, 90)

        v_layout = QtWidgets.QVBoxLayout(widget)

        h1_layout = QtWidgets.QHBoxLayout()
        h1_layout.addStretch()
        h1_layout.addWidget(self.BackButton)

        v_layout.addStretch(3)
        h2_layout = QtWidgets.QHBoxLayout()
        h2_layout.addStretch()

        h2_layout.addWidget(self.label)
        # h2_layout.addWidget(self.label1)
        h2_layout.addStretch()
        v_layout.addLayout(h2_layout)

        h3_layout = QtWidgets.QHBoxLayout(widget)
        h3_layout.addStretch()
        h3_layout.addWidget(self.text)
        h3_layout.addStretch()
        v_layout.addLayout(h3_layout)
        # Create the button and set its properties

        v_layout.addStretch(5)
        v_layout.addLayout(h1_layout)

        self.setLayout(v_layout)

    def back_to_main(self):
        self.goto("main")
