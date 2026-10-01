import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
)

price = 500000

def bardasht():
    global price
    tex = Qline.text()

    if tex == "":
        QMessageBox.warning(win, 'warning', 'لطفا فیلد را کامل کنید.')
        return

    try:
        int_pr = int(tex)
    except ValueError:
        QMessageBox.warning(win, 'warning', 'لطفا مبلغ معتبر وارد کنید')
        return

    if int_pr <= 0:
        QMessageBox.warning(win, 'warning', 'عدد وارد شده باید از صفر بزرگ‌تر باشد')
        return

    if int_pr > price:
        QMessageBox.warning(win, 'warning', 'موجودی ناکافی است')
        return

    price -= int_pr
    QMessageBox.information(win, 'رسید', f'مبلغ {int_pr} با موفقیت برداشت شد')
    label_pr.setText(f'موجودی فعلی: {price}')

def namyesh():
    global price
    QMessageBox.information(win, 'موجودی', f'موجودی شما: {price}')

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("hkode pardaz")
win.resize(500, 300)
win.setStyleSheet("""
    QWidget { background-color: #F3F6FA; }
    QLabel { color: #263238; font-size: 16px; }
""")

label_1 = QLabel('برنامه حسابداری', win)
label_1.move(220, 30)
label_1.setStyleSheet("font-size:15px; font-weight:bold;")


label_pr = QLabel('مبلغ اولیه: 500000', win)
label_pr.move(350, 80)
label_pr.setStyleSheet("font-size:15px; font-weight:bold;")


label = QLabel('مبلغ را وارد کنید:', win)
label.move(360, 120)
label.setStyleSheet("font-size:15px; font-weight:bold;")


Qline = QLineEdit(win)
Qline.setGeometry(110, 170, 350, 40)
Qline.setPlaceholderText('مثال: 100000')
Qline.setStyleSheet("""
    QLineEdit {
        background-color: white;
        border: 2px inset #CFD8DC;
        border-radius: 8px;
        padding: 6px;
        font-size: 15px;
    }
    QLineEdit:focus { border: 2px inset #1976D2; }
""")

Qp_bardasht = QPushButton('برداشت', win)
Qp_bardasht.setGeometry(70, 230, 170, 40)
Qp_bardasht.setStyleSheet("""
    QPushButton {
        font-size: 15px;  background-color: #74b9ff; border-radius: 10px;
    }
    QPushButton:hover { background-color: #0984e3; }
    QPushButton:pressed { background-color: #0984e3; border: 2px solid #000; }
""")


Qp_namyesh = QPushButton('نمایش موجودی', win)
Qp_namyesh.setGeometry(280, 230, 170, 40)
Qp_namyesh.setStyleSheet(""" 
    QPushButton {
        font-size: 15px;  background-color: #74b9ff; border-radius: 10px;
    }
    QPushButton:hover { background-color: #0984e3; }
    QPushButton:pressed { background-color: #0984e3; border: 2px solid #000; }
""")


Qp_bardasht.clicked.connect(bardasht)
Qp_namyesh.clicked.connect(namyesh)
win.show()
sys.exit(app.exec())
