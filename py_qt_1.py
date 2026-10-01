from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton
import sys
#app and window 
app=QApplication(sys.argv)
win=QWidget()
win.setWindowTitle("برنامه من ")
win.resize(800,500)
# win.move()
win.setStyleSheet("""
background-color:#2d6e7e;
""")

#qlabel
#meli

qLabel_mel=QLabel('کد ملی : ', win)
qLabel_mel.move(690,50)
qLabel_mel.setStyleSheet("""
font-size:26px;
color:white
""")
#name 

qLabel_name=QLabel('نام : ', win)
qLabel_name.move(740,80)
qLabel_name.setStyleSheet("""
font-size:26px;
color:white
""")

#family 

qLabel_fam=QLabel('نام خانوادگی :  ', win)
qLabel_fam.move(630,110)
qLabel_fam.setStyleSheet("""
font-size:26px;
color:white
""")

#shomare

qLabel_number=QLabel('شماره : ', win)
qLabel_number.move(710,140)
qLabel_number.setStyleSheet("""
font-size:26px;
color:white
""")

#qline edit 
#kod meli 
input_mel=QLineEdit(win)
input_mel.move(490,60)
input_mel.setStyleSheet("""
font-size:14px;
color:black
""")

# name

input_name=QLineEdit(win)
input_name.move(490,90)
input_name.setStyleSheet("""
font-size:14px;
color:black
""")

#fam

input_fam=QLineEdit(win)
input_fam.move(490,120)
input_fam.setStyleSheet("""
font-size:14px;
color:black
""")

#shom

input_fam=QLineEdit(win)
input_fam.move(490,150)
input_fam.setStyleSheet("""
font-size:14px;
color:black
""")

#butoon

button=QPushButton('ثبت',win)
button.move(350,450)
button.setStyleSheet("""
font-size:20px;
background-color:green
""")

# border-raduise:green




win.show()
sys.exit(app.exec())