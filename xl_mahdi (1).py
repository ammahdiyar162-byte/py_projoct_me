import sys

from openpyxl import Workbook

book = Workbook()
sheet = book.active
sheet.append(['Name', 'Family','Age'])

#-----def-------
def ADD():

    N=input('Enter name :')
    F=input('Enter Family :')
    AG=input('Enter Age :')

    sheet.append([N, F, AG])

def SH():
    for r in sheet.iter_rows():
        print(r[0].value,r[1].value,r[2].value)

def SV():
    print("Saving....")
    book.save('mahdi.xlsx')


while True :
    print('--- Menu ---')
    print('1 --- Add')
    print('2 --- Show')
    print('3 --- Save')
    print('4 --- Exit')

    z=int(input('enter number in menu (1-4) : '))

    if z == 1 :
        ADD()
    if z == 2 :
        SH()
    if z == 3 :
        SV()
    if z == 4 :
        SV()
        break
