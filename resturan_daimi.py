#sistem modiriat 1 resturan
import json
import os 
resturan={
    'mahi': 5,
    'kabab': 10,
    'morgh': 2,
    'sooshi': 7,
    'mahiche': 0,
    'pizaa(morgh)': 5,
    'pizaa(peperoni)': 8

}

# baraye zakhire etelaat be sorate daemi
FILE_NAME = 'resturan.json'

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as file:
        resturan = json.load(file)
else:
    with open(FILE_NAME, 'w') as file:
        json.dump(resturan, file)


def save():
    with open(FILE_NAME, 'w') as file:
        json.dump(resturan, file)


def show():
    for name ,moj  in resturan.items() :
        print(name ,':', moj ) 


def add():
    name=input('enter name food :').lower()
    mojoodi=int(input('entre mojoodi ghaza baraye emroz :'))
    if name in resturan:
        print('kala mojood ast')
        if mojoodi== 0 :
            print('moojodi ashanemitavanad 0 bd !!')
    else:
        resturan[name]=mojoodi
        save()
        print('added ...')

def delet():
    show()

    name=input('enter name food :').lower()
    if name in resturan:
        del resturan[name]
        save()
        print('deleted ...')
    else :
        print('food mored nazar in resturan nist')
        
def sefaresh():

    print('--- menu resturan ---')
    show()
    n_food=input('enter name food :').lower()
    tedad=int(input('enter tedad mored nazar  :'))
    if n_food in resturan:
        
        if resturan[n_food] >0:
            resturan[n_food]=resturan[n_food]-tedad
            save()
            print('sefaresh sabt shode :) ')
        else :
            print('tedad mored nazar shoma mojood nist , soryy mojoodi :',resturan[n_food] ) 
    else :
        print('food mored nazar in resturan moojood nist')

def cancel_s():
    name_f=input('enter name food :').lower()
    tedad_c=int(input('enter tedad food for cancel :'))
    if name_f in resturan:
        resturan[name_f]=resturan[name_f]+tedad_c
        save()
        print('cancel shode')
    else :
        print('not found your food in resturan !!')

def peygham():
    peygham={

    }
    payam=input('enter peygham :')
    name=input('enter name foe sabt :')
    if name in peygham:
        print('name shoma dar list hast ... agar motmaen hastid ba name digari vared shavid ')
    else :
        peygham[payam]=name
print(' peygham sabt shode ast ')

def show_payam():
    pas=123456
    
    for x in range(3):
        pasword=int(input('enter pasword please :'))
        if pasword==pas :
            print(peygham)
        else :
            print('paswor eshtebah ast')
        if x == 3:
            print(' bish az 3 talash na mofagh baraname baste mishavad ') 
            break

while True:

    print('\n-----Menu-----')
    print('1-- show ghaza ha ')
    print('2-- add food ')
    print('3-- delet food ')
    print('4-- sefaresh ghaza ')
    print('5-- cancel kardan sefaresh ')
    print('6-- peygham moshtari ')
    print('7-- show peygham mostari(modiriat!!)')
    print('8-- exit resturan :( ')

    choice=int(input('enter number in menu :'))

    if choice == 1 :
        show()
    elif choice == 2 :
        add()
    elif choice == 3 :
        delet()
    elif choice == 4 :
        sefaresh()
    elif choice == 5 :
        cancel_s()
    elif choice == 6 :
        peygham()
    elif choice == 7 :
        show_payam() 
    elif choice == 8 :
        print('good day :)')
        break