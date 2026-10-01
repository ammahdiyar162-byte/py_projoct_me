from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit
import sys

#-------------توابع-------------

def big():
    label.setText(input.text())
    label.setStyleSheet("""
    color:black;
    font-size:35px;
    font-weight:bold;
    """)

def rredd():
    label.setText(input.text())
    label.setStyleSheet("""
    color:red;
    font-size:25px;
    font-weight:bold;
    """)

def clear():
    input.clear()
    label.clear()


#app and window

app=QApplication(sys.argv)
win=QWidget()
win.setWindowTitle("text_edit")
win.resize(600,300)
win.move(700,300)
win.setStyleSheet("background-color:#e4e4e4;")


#-----------برنامه اصلی------------

label=QLabel('py_class',win)
label.move(240,40)
label.setStyleSheet("""
color:black;
font-size:25px;
font-weight:bold;
""")

input=QLineEdit(win)
input.move(150,110)
input.resize(300,40)

bigg=QPushButton('Big',win)
bigg.move(60,200)
bigg.resize(120,45)
bigg.setStyleSheet("""
QPushButton{
    color:white;
    background-color:#2885f8;
    border-radius:10px;
    font-size:15px;
}
QPushButton:hover{background-color:#6ab0ff;}
QPushButton:pressed{background-color:#0d5fc9;}
""")

red=QPushButton('Red',win)
red.move(240,200)
red.resize(120,45)
red.setStyleSheet("""
QPushButton{
    color:white;
    background-color:#ff3d3d;
    border-radius:10px;
    font-size:15px;
}
QPushButton:hover{
    background-color:#ff8080;
}
QPushButton:pressed{
    background-color:#cc0000;
}
""")

clered=QPushButton('clear',win)
clered.move(420,200)
clered.resize(120,45)
clered.setStyleSheet("""
QPushButton{
    color:white;
    background-color:#7a7979;
    border-radius:10px;
    font-size:15px;
}
QPushButton:hover{
    background-color:#a3a3a3;
}
QPushButton:pressed{
    background-color:#555555;
}
""")

bigg.clicked.connect(big)
red.clicked.connect(rredd)
clered.clicked.connect(clear)

win.show()
sys.exit(app.exec())