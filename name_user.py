from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QMessageBox,QLineEdit
import sys

#-------------توابع-------------


def pas_us():
    us=txt1.text()
    ps=txt2.text()

    user='mahdiyar'
    pas='12345'

    if us==user and ps==pas:
        QMessageBox.information(
            win,
            'ثبت',
            'به کلاس پایتون خوش آمدید'
        )
    else :
        QMessageBox.warning(
            win,
            'خطا',
            'اطلاعات خود را کاما کنید'
        )


def clear():
    txt1.clear()
    txt2.clear()









#app and window

app=QApplication(sys.argv)
win=QWidget()
win.setWindowTitle("QMessageBox")
win.resize(700,300)
# win.move(300,200)
win.setStyleSheet("background-color:#f7e6c5")





#-----------برنامه اصلی------------

#labels

    #user

label_1=QLabel('نام کاربری' ,win)
label_1.move(500,57)
label_1.setStyleSheet("""
font-size:15px;
color: #797436;
font-weight: bold;
""")

    #pas

label_2=QLabel('پسورد ',win)
label_2.move(500,92)
label_2.setStyleSheet("""
font-size:15px;
color: #797436;
font-weight: bold;
""")

#Qlineedit
    #Ql_user

txt1=QLineEdit(win)
txt1.setGeometry(250,50,200,30)
txt1.setPlaceholderText("لطفا نام کاربری خود را وارد کنید")
txt1.setStyleSheet("""
font-weight:bold;
""")
    #ql_pas
txt2=QLineEdit(win)
txt2.setGeometry(250,90,200,30)
txt2.setPlaceholderText("لطفا پسورد خود را وارد کنید")
txt2.setStyleSheet("""
font-weight:bold;
color:black;
""")

#QPushButton
sabt=QPushButton('ثبت', win)
sabt.setGeometry(200,200,100,40)
sabt.setStyleSheet("""
QPushButton {
        font-size:20px;
        color:black;
        background-color: green;
        border-radius:10px;
}
    QPushButton:hover {
        background-color: #26ea46;
    }
        QPushButton:pressed 
    {
        background-color: #116c38;
        }
""")


#QPushButton
cl=QPushButton('پاک کردن', win)
cl.setGeometry(400,200,100,40)
cl.setStyleSheet("""
QPushButton {
        font-size:20px;
        color:black;
        background-color: #7a7979;
        border-radius:10px;
}
QPushButton:hover{
    background-color:#a3a3a3;
}
QPushButton:pressed{
    background-color:#555555;
}
""")


cl.clicked.connect(clear)
sabt.clicked.connect(pas_us)

win.show()
sys.exit(app.exec())
