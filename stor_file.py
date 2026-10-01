import sys
import os
from openpyxl import Workbook , load_workbook
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

FILE='store.xlsx'

#----defs------

def create():
    if not os.path.exists(FILE):
        book=Workbook()
        sheet.title = 'کالاها' 
        sheet=book.active
        sheet["A1"]='کد کالا '
        sheet['B1']='نام کالا'
        sheet['C1']="قیمت کالا"
        sheet['C1']="تعداد موجودی"
        book.save(FILE)



def sabt():
    code=texbox_code.text()
    name=texbox_name.text()
    price=texbox_pr.text()
    mj=texbox_mojoodi.text()

    if code=="":
        QMessageBox.warning(
            win,
            'warning',
            'لطفا کد کالا را خالی نزارید'
        )
        return

    if name=="":
        QMessageBox.warning(
            win,
            'warning',
            'لطفا نام کالا را خالی نزارید'
        )
        return

    if price=="":
        QMessageBox.warning(
        win,
        'warning',
        'لطفا قیمت کالا را خالی نزارید'
        )
        return

    if mj=="":
        QMessageBox.warning(
        win,
        'warning',
        'لطفا قیمت کالا را خالی نزارید'
        )
        return

    if not code.isdigit():
        QMessageBox.warning(
            win,
            'warning',
            'کد کالا باید به عدد باشد '
        )
        return

    if not price.isdigit():
        QMessageBox.warning(
            win,
            'warning',
            'قیمت کالا باید به عدد باشد '
        )
        return

    if not mj.isdigit():
        QMessageBox.warning(
            win,
            'warning',
            'موجودی کالا باید به عدد باشد '
        )
        return

    book=load_workbook(FILE)
    sheet = book['کالا ها']
    sheet.append([int(code) , int(name) , int(price) , int(mj)])
    book.save(FILE)
    book.close()

def show_kala():
    if not os.path.exists(FILE):
        QMessageBox.information(
            win,
            'کالا',
            'هیچ کالایی ثبت نشده است '
        )
        return

    book= load_workbook(FILE)
    sheet= book['کالا ها ']
    r=sheet.iter_rows(min_row=2 , values_only=True)

    qty=0
    text=''
    c=0
    for row in r :
        if row[0] is None:
            continue

        code, name , price , mj = row
        c += 1
        qty += qty
        text+= f'کد کالا :{code}\n'
        text+= f'کد کالا :{name}\n'
        text+= f'کد کالا :{price}\n'        
        text+= f'کد کالا :{mj}\n'    
        text+= '---\n' 

    text += f'\n تعداد کالا های ثبت شده :{c}\n'
    text += f'\n مجموع موجودی کالا ها  :{c}\n '
    book.close()
    QMessageBox.information(
        win,
        'kala ha ',
        'گزارش ها'
    )




def clear():
    a=(texbox_code,texbox_name,texbox_pr,texbox_mojoodi)
    
    A = QMessageBox.question(
        win,
        "سوال",
        "آیا مطمئن هستید که اطلاعات پاک شود؟",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    )
    if A == QMessageBox.StandardButton.Yes:
        texbox_code.clear()
        texbox_name.clear()
        texbox_pr.clear()
        texbox_mojoodi.clear()

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('store')
win.resize(500,450)

#----label----

label=QLabel('مدریت فروشگاه',win)
label.setGeometry(150,30,150,35)
label.setStyleSheet("""
font-size: 15px;
font-weight:bold;
color-black;
background-color: 
""")


label_code=QLabel('کد کالا',win)
label_code.move(380, 85)
label_code.resize(100, 35)
label_code.setStyleSheet("""
color: #263238;
font-size: 14px;
font-weight:bold;
""")

label_name=QLabel('نام کالا',win)
label_name.move(385, 135)
label_name.resize(100, 35)
label_name.setStyleSheet("""
color: #263238;
font-size: 14px;
font-weight:bold;
""")

label_name=QLabel('قیمت کالا ',win)
label_name.move(390, 185)
label_name.resize(100, 35)
label_name.setStyleSheet("""
color: #263238;
font-size: 14px;
font-weight:bold;
""")


label_name=QLabel('موجودی کالا ',win)
label_name.move(400, 235)
label_name.resize(100, 35)
label_name.setStyleSheet("""
color: #263238;
font-size: 14px;
font-weight:bold;
""")

#texbox

texbox_code=QLineEdit(win)
texbox_code.setGeometry(105, 90, 300, 35)
texbox_code.setPlaceholderText('مثال: 109')
texbox_code.setStyleSheet("""
QLineEdit {
    background-color: white;
    border: 2px inset #CFD8DC;
    border-radius: 8px;
    padding: 6px;
    font-size: 15px;
}
    QLineEdit:focus { border: 2px inset #1976D2; }
""")

texbox_name=QLineEdit(win)
texbox_name.setGeometry(105, 135, 300, 35)
texbox_name.setPlaceholderText('مثال: کیبورد')
texbox_name.setStyleSheet("""
QLineEdit {
    background-color: white;
    border: 2px inset #CFD8DC;
    border-radius: 8px;
    padding: 6px;
    font-size: 15px;
}
    QLineEdit:focus { border: 2px inset #1976D2; }
""")


texbox_pr=QLineEdit(win)
texbox_pr.setGeometry(105, 180, 300, 35)
texbox_pr.setPlaceholderText('مثال: 200,000')
texbox_pr.setStyleSheet("""
QLineEdit {
    background-color: white;
    border: 2px inset #CFD8DC;
    border-radius: 8px;
    padding: 6px;
    font-size: 15px;
}
    QLineEdit:focus { border: 2px inset #1976D2; }
""")


texbox_mojoodi=QLineEdit(win)
texbox_mojoodi.setGeometry(105, 230, 300, 35)
texbox_mojoodi.setPlaceholderText('مثال: 12')
texbox_mojoodi.setStyleSheet("""
QLineEdit {
    background-color: white;
    border: 2px inset #CFD8DC;
    border-radius: 8px;
    padding: 6px;
    font-size: 15px;
}
    QLineEdit:focus { border: 2px inset #1976D2; }
""")


#Qpushbtn

btn_sabt=QPushButton('ثبت', win)
btn_sabt.setGeometry(265, 280, 140, 40)
btn_sabt.setStyleSheet(""" 
    QPushButton {
        font-size: 15px;  background-color: #30c342; border-radius: 10px;
    }
    QPushButton:hover { background-color: #59d668; }
    QPushButton:pressed { background-color: #20832a; border: 2px solid #000; }
""")



btn_clear=QPushButton('پاک کردن', win)
btn_clear.setGeometry(105, 280, 140, 40)
btn_clear.setStyleSheet(""" 
    QPushButton {
        font-size: 15px;  background-color: #696969; border-radius: 10px;
    }
    QPushButton:hover { background-color: #969696; }
    QPushButton:pressed { background-color: #4e4e4e; border: 2px solid #000; }
""")

btn_gozaresh=QPushButton('گزارش کالا', win)
btn_gozaresh.setGeometry(105, 330, 300, 40)
btn_gozaresh.setStyleSheet(""" 
    QPushButton {
        font-size: 15px;  background-color: #74b9ff; border-radius: 10px;
    }
    QPushButton:hover { background-color: #a0d3fa; }
    QPushButton:pressed { background-color: #0984e3; border: 2px solid #000; }
""")

btn_clear.clicked.connect(clear)
btn_sabt.clicked.connect(sabt)
btn_gozaresh.clicked.connect(show_kala)

create()
win.show()
sys.exit(app.exec())
