
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)
from PyQt6.QtCore import Qt


def show():
    QMessageBox.information(
        win,
        'خوش آمد',
        'به برنامه خوش آمدید'
    )



app=QApplication(sys.argv)
app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
win=QMainWindow()
win.resize(500,300)
win.setWindowTitle('منو')


menu=win.menuBar()

file_menu= menu.addMenu('پیام')
edit_menu= menu.addMenu('ویرایش')
hellp_menu= menu.addMenu('راهنما')
exit_menu= menu.addMenu('خروج')

mds=file_menu.addAction('پیام')

ms_action=edit_menu.addAction('کپی')
ms_action=edit_menu.addAction('چسباندن')

mss_action= hellp_menu.addAction('راهنما')
mss_action= hellp_menu.addAction('پشتیبانی')
mss_action= hellp_menu.addAction('تماس با ما')

ex=exit_menu.addAction('خروج')
msss_action= exit_menu.addAction('ذخیره ')

mds.triggered.connect(show)
exit_menu.triggered.connect(win.close)



win.show()
sys.exit(app.exec())
