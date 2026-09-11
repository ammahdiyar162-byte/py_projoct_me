from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QMessageBox,QLineEdit
import sys


#-------------توابع-------------
pr_pizaa=600000
pr_drink=30000

def calc():
    name=Ql_name.text()
    piz=Ql_pizaa.text()
    dr=Ql_drink.text()

    if name=="" or piz=="" or dr=="":
        QMessageBox.warning(
            win,
            'هشدار',
            'لطفا اطلاعات را کامل کنید'
        )
        return
#برسی عدد بودن

    if not piz.isdigit() or not dr.isdigit():
        QMessageBox.critical(
            win,
            'خطا',
            'خطا، لطفا پیتزا و نوشایه رو به عدد  وارد کنید'
        )
        return



#تبدیل به عدد از استرینگ
    
    piz=int(piz)
    dr=int(dr)

    mohasebe=piz * pr_pizaa + dr * pr_drink
    tahkfif = mohasebe * 0.1 if piz >= 3 else 0

    pr_final=mohasebe-tahkfif

    #ersal +2m
    
    if pr_final>2000000:
        mg='ارسال غذا شما رایگان است'
    else :
        mg='ارسال غذا شما جدا گانه حساب می شود '
#faktoor
    QMessageBox.information(
        win, 'فاکتور سفارش',
        f'نام مشتری: {name}\n'
        f'تعداد پیتزا: {piz}\n'
        f'تعداد نوشابه: {dr}\n\n'
        f'مبلغ اولیه: {mohasebe:,} تومان\n'
        f'تخفیف: {tahkfif:,.0f} تومان\n'
        f'مبلغ نهایی: {pr_final:,.0f} تومان\n\n'
        f'{mg}'
    )



#app and window

app=QApplication(sys.argv)
win=QWidget()
win.setWindowTitle("QMessageBox")
win.resize(600,600)
# win.move(300,200)
win.setStyleSheet("background-color:#f7e6c5;")


def clear():
    Ql_name.clear()
    Ql_pizaa.clear()
    Ql_drink.clear()


#-----------برنامه اصلی------------

#label-pizaa

label=QLabel('سفارش پیتزا',win)
label.move(180,50)
label.setStyleSheet("""
font-size:45px;
color: #black;
font-weight: none;
""")

#label-name

label_1=QLabel('نام مشتری',win)
label_1.move(440,178)
label_1.setStyleSheet("""
font-size:22px;
color: black;
""")

#label-pizaa1


label_2=QLabel('تعداد پیتزا',win)
label_2.move(450,248)
label_2.setStyleSheet("""
font-size:22px;
color: black;
""")

#label-drink

label_1=QLabel('تعداد نوشابه',win)
label_1.move(430,320)
label_1.setStyleSheet("""
font-size:22px;
color: black;
""")

#Qline-name

Ql_name=QLineEdit(win)
Ql_name.setGeometry(100,180,260,35)
Ql_name.setPlaceholderText('لطفا نام خود را وارد کنید..')
Ql_name.setStyleSheet("""
font-weight:none;
font-size:14px;
border-radius:12px;
color-black;
background-color:white;
""")

#Qline-pizaa

Ql_pizaa=QLineEdit(win)
Ql_pizaa.setGeometry(100,250,260,35)
Ql_pizaa.setPlaceholderText('لطفا تعداد پیتزا خود را وارد کنید...')
Ql_pizaa.setStyleSheet("""
font-weight:none;
font-size:14px;
border-radius:12px;
color-black;
background-color:white;
""")

#Qline-drink

Ql_drink=QLineEdit(win)
Ql_drink.setGeometry(100,320,260,35)
Ql_drink.setPlaceholderText('لطفا تعداد نوشابه خود را وارد کنید...')
Ql_drink.setStyleSheet("""
font-weight:none;
font-size:14px;
border-radius:12px;
color-black;
background-color:white;
""")


#QPushButton-sabt

Qp_sabt=QPushButton('محاسبه سفارش', win)
Qp_sabt.setGeometry(150,400,150,50)
Qp_sabt.setStyleSheet("""
QPushButton {
        font-size:15px;
        font-weight:bold;
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

Qp_sabt.clicked.connect(calc)

#Qp-clear
cl=QPushButton('پاک کردن', win)
cl.setGeometry(150,480,150,50)
cl.setStyleSheet("""
QPushButton {
        font-size:15px;
        font-weight:bold;
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

#اجرا

win.show()
sys.exit(app.exec())