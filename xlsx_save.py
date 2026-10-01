import sys

from openpyxl import Workbook

book = Workbook()
sheet = book.active
sheet.append(['Name', 'Family','Age'])

#-----def-------
def add():

    name=input('Enter name :')
    fam=input('Enter Family :')
    age=input('Enter Age :')

    sheet.append([name, fam, age])

def Show():
    for row in sheet.iter_rows():
        print(row[0].value,row[1].value,row[2].value)

def save():
    print("Saving and exiting...")
    book.save('st.xlsx')


while True :
    print('--- Menu ---')
    print('1 --- Add')
    print('2 --- Show')
    print('3 --- Save')
    print('4 --- Exit')

    w=int(input('enter number in menu (1-4) : '))

    if w == 1 :
        add()
    if w == 2 :
        Show()
    if w == 3 :
        save()
    if w == 4 :
        save()
