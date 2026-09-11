from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QPushButton
import sys

#-------------توابع-------------

def green():
    label.setText('green')
    label.setStyleSheet("""
    font-size:45px;
    color:green;
    """)

def yellow():
    label.setText('yellow')
    label.setStyleSheet("""
    font-size:45px;
    color:yellow;
    """)

def red():
    label.setText('red')
    label.setStyleSheet("""
    font-size:45px;
    color:red;
    """)

#app and window

app=QApplication(sys.argv)
win=QWidget()
win.setWindowTitle("برنامه من ")
win.resize(800,400)
win.move(300,200)
win.setStyleSheet("background-color:white")



label= QLabel('چراغ راهنما',win)
label.move(300,130)
label.setStyleSheet("""
font-size:35px;
color:black;
font-weight:bold;
""")

#-----------------دکمه ها-----------------

#green
btn_green=QPushButton('green',win)
btn_green.move(500,250)
btn_green.resize(100, 50)
btn_green.setStyleSheet("""
QPushButton{
    background-color:green;
    color:white;
    border-radius:15px;
    font-size:18px;
    font-weight:bold;
}
QPushButton:hover{
    background-color:#006400;
    color:white;
}
QPushButton:pressed{
    background-color:#006400;
    color:white;
}
""")
btn_green.clicked.connect(green)

#yellow
btn_yeloo=QPushButton('yellow',win)
btn_yeloo.move(350,250)
btn_yeloo.resize(100,50)
btn_yeloo.setStyleSheet("""
QPushButton{
    background-color:yellow;
    color:white;
    border-radius:15px;
    font-size:18px;
    font-weight:bold;
}
QPushButton:hover{
    background-color:#ffff5a;
    color:white;
}
QPushButton:pressed{
    background-color:#f5f500;
    color:white;
}
""")
btn_yeloo.clicked.connect(yellow)

#red
btn_red=QPushButton('red',win)
btn_red.move(200,250)
btn_red.resize(100,50)
btn_red.setStyleSheet("""
QPushButton{
    background-color:red;
    color:white;
    border-radius:15px;
    font-size:18px;
    font-weight:bold;
}
QPushButton:hover{
    background-color:#ff4646;
    color:white;
}
QPushButton:pressed{
    background-color:#c30000;
    color:white;
}
""")
btn_red.clicked.connect(red)

win.show()
sys.exit(app.exec())
