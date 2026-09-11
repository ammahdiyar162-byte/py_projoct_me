from PyQt6.QtWidgets import QApplication, QWidget,QLineEdit,QLabel,QPushButton
import sys

def clear() :
    input_file.clear()

def red() :
    text.setStyleSheet("""
    color:red;
    font-size:25px;
    font-weight:bold;
    """)

def zoom() :
    text.setStyleSheet("""
    color:black;
    font-size:30px;
    font-weight:bold;
    """)

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('برنامه ویرایش متن')
window.move(700,300)
window.resize(600,300)
window.setStyleSheet("""
background-color:#e4e4e4;
""")

text=QLabel('کلاس پایتون',window)
text.move(240,50)
text.setStyleSheet("""
color:black;
font-size:25px;
font-weight:bold;
""")

input_file=QLineEdit(window)
input_file.move(160,100)
input_file.resize(300,30)

b_clear=QPushButton('🗑 پاک کن',window)
b_clear.move(400,200)
b_clear.resize(110,40)
b_clear.setStyleSheet("""
color:white;
background-color:#7a7979;
border-radius:10px;
font-weight:bold;
font-size:15px;
""")

b_red= QPushButton('🔴 قرمز',window)
b_red.move(250,200)
b_red.resize(110,40)
b_red.setStyleSheet("""
color:white;
background-color:#ff3d3d;
border-radius:10px;
font-weight:bold;
font-size:15px;
""")

b_zoom=QPushButton('🔍 بزرگ',window)
b_zoom.move(100,200)
b_zoom.resize(110,40)
b_zoom.setStyleSheet("""
color:white;
background-color:#2885f8;
border-radius:10px;
font-weight:bold;
font-size:15px;
""")

b_clear.clicked.connect(clear)

b_red.clicked.connect(red)

b_zoom.clicked.connect(zoom)


window.show()

sys.exit(app.exec())