from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QMessageBox
import sys

#-------------توابع-------------

def fun1():
    QMessageBox.information(
        win,
        'ثبت',
        'اطلاعات با موفقیت ثبت شد'
    )

def fun2():
        QMessageBox.warning(
        win,
        'خطا',
        'اطلاعات خود را کاما کنید'
    )

def fun3():
      QMessageBox.critical(
            win,
            'اخطار',
            'عملیات با خطا مواجه شد'
      )


#app and window

app=QApplication(sys.argv)
win=QWidget()
win.setWindowTitle("QMessageBox")
win.resize(700,300)
# win.move(300,200)
win.setStyleSheet("background-color:white")


#-----------برنامه اصلی------------

label=QLabel('یک گزیه را انتخاب کنید ...',win)
label.move(250,50)
label.setStyleSheet("""
font-size:20px;
font-weight:bold;
""")


btn_1=QPushButton('ثبت',win)
btn_1.setGeometry(200,100,100,50)
btn_1.setStyleSheet("""
    QPushButton {
        font-size: 20px;
        font-weight: bold;
        background-color:#30bf04;
        color: #1F3A5F;

        border-radius: 10px;
        border-none;
    }
    QPushButton:hover {
        background-color: #26ea46;
    }
    QPushButton:pressed 
    {
        background-color: #116c38;
        }
""")

btn_2=QPushButton('خطا',win)
btn_2.setGeometry(350,100,100,50)
btn_2.setStyleSheet("""
QPushButton {
    font-size: 20px;
    font-weight: bold;
    background-color:#FF8C00;
    color: #1F3A5F;

    border-radius: 10px;
    border-none;
}
QPushButton :hover {background-color:#ffb250;}
QPushButton :pressed {background-color:#e17a00;}
    QPushButton:hover {
        background-color: #ffb250;
    }
    QPushButton:pressed 
    {
        background-color: #e17a00;
        }
""")


btn_3=QPushButton('هشدار',win)
btn_3.setGeometry(500,100,100,50)
btn_3.setStyleSheet("""
QPushButton {
    font-size: 20px;
    font-weight: bold;
    background-color:#FF0000;
    color: #1F3A5F;

    border-radius: 10px;
    border-none;
}
QPushButton :hover {background-color:#ffb250;}
QPushButton :pressed {background-color:#e17a00;}
    QPushButton:hover {
        background-color: #ff3232;
    }
    QPushButton:pressed 
    {
        background-color: #cd0000;
        }
""")

btn_1.clicked.connect(fun1)
btn_2.clicked.connect(fun2)
btn_3.clicked.connect(fun3)





win.show()
sys.exit(app.exec())
