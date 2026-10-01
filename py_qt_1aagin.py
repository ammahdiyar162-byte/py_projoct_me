from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

import sys 
Ap=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('برنامه من دوباره')
window.resize(800,500)
window.setStyleSheet("""
background-color:#2d6e7e;
""")
#Qlabel
#name  and fam

name_qlabel=QLabel('نام و نام',window)
name_qlabel.move(700,90)
name_qlabel.setStyleSheet("""
font-size:24px
color:black
""")

name_qline=QLineEdit(window)
name_qline.move(550,90)
name_qline.setStyleSheet("""
font-size:24px
color:black
""")




button=QPushButton('ثبت', window)
button.move(350,460)
button.setStyleSheet("""
font-size:20px;
background-color:green

""")












#---------------------------------------------------------------------------------------------------------
window.show()
sys.exit(Ap.exec())