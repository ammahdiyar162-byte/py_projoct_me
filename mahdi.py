import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt

# Motaghayere asli
mablagh_mojoodi = 500000

def amaliyat_bardasht():
    global mablagh_mojoodi
    matn_voroodi = voroodi_mablagh.text()

    if matn_voroodi == "":
        QMessageBox.warning(panjere_asli, 'Hoshdar', 'Lotfan field ra kamel konid.')
        return

    try:
        adad_voroodi = int(matn_voroodi)
    except ValueError:
        QMessageBox.warning(panjere_asli, 'Hoshdar', 'Lotfan mablagh motabar vared konid.')
        return

    if adad_voroodi <= 0:
        QMessageBox.warning(panjere_asli, 'Hoshdar', 'Adad vared shode bayad az sefr bozorgtar bashad.')
        return

    if adad_voroodi > mablagh_mojoodi:
        QMessageBox.warning(panjere_asli, 'Hoshdar', 'Mojoodi nakafi ast.')
        return

    mablagh_mojoodi -= adad_voroodi
    QMessageBox.information(panjere_asli, 'Resid', f'Mablagh {adad_voroodi} ba movafaghiyat bardasht shod.')
    label_mojoodi.setText(f'Mojoodi fe\'li: {mablagh_mojoodi}')

def namayesh_mablagh():
    global mablagh_mojoodi
    QMessageBox.information(panjere_asli, 'Mojoodi', f'Mojoodi shoma: {mablagh_mojoodi}')

# Sakhtar barname
barname = QApplication(sys.argv)
panjere_asli = QWidget()
panjere_asli.setWindowTitle("Barname Hesabdari")
panjere_asli.resize(400, 300)
panjere_asli.setStyleSheet("QWidget { background-color: #F7F7F9; }")

# Estefade az Layout baraye moratab sazi (Layout-based design)
layout_asli = QVBoxLayout()
layout_asli.setContentsMargins(30, 30, 30, 30) # Fasle az kenareha
layout_asli.setSpacing(15)

# Labelha
titr_barname = QLabel('Barname Hesabdari')
titr_barname.setStyleSheet("font-size:18px; font-weight:bold; color: #333333;")
titr_barname.setAlignment(Qt.AlignCenter) # Vasat chin

label_mojoodi = QLabel(f'Mablagh avaliye: {mablagh_mojoodi}')
label_mojoodi.setStyleSheet("font-size:14px; color: #555555;")
label_mojoodi.setAlignment(Qt.AlignLeft) # Samte chap

rahnamaye_vorood = QLabel('Mablagh ra vared konid:')
rahnamaye_vorood.setStyleSheet("font-size:14px; color: #555555;")
rahnamaye_vorood.setAlignment(Qt.AlignLeft) # Samte chap

voroodi_mablagh = QLineEdit()
voroodi_mablagh.setPlaceholderText('Mesal: 100000')
voroodi_mablagh.setStyleSheet("""
    QLineEdit {
        background-color: #FFFFFF;
        border: 2px solid #D1D5DB;
        border-radius: 8px;
        padding: 10px;
        font-size: 15px;
    }
    QLineEdit:focus { border: 2px solid #F472B6; }
""")

# Layout baraye dokmeha
layout_dokmeha = QHBoxLayout()
dokme_bardasht = QPushButton('Bardasht')
dokme_namayesh = QPushButton('Namayesh')

# Styling dokmeha
for btn in [dokme_bardasht, dokme_namayesh]:
    btn.setStyleSheet("""
        QPushButton {
            font-size: 14px;
            background-color: #FBCFE8;
            color: #831843;
            border-radius: 8px;
            padding: 8px;
            border: none;
        }
        QPushButton:hover { background-color: #F472B6; color: #FFFFFF; }
    """)

layout_dokmeha.addWidget(dokme_bardasht)
layout_dokmeha.addWidget(dokme_namayesh)

# Afzoodan be layout asli
layout_asli.addWidget(titr_barname)
layout_asli.addSpacing(10)
layout_asli.addWidget(label_mojoodi)
layout_asli.addWidget(rahnamaye_vorood)
layout_asli.addWidget(voroodi_mablagh)
layout_asli.addLayout(layout_dokmeha)

panjere_asli.setLayout(layout_asli)

# Konekt kardan
dokme_bardasht.clicked.connect(amaliyat_bardasht)
dokme_namayesh.clicked.connect(namayesh_mablagh)

panjere_asli.show()
sys.exit(barname.exec())
