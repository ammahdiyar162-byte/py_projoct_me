#sistem modiriat 1 resturan 
resturan={
    'mahi': 5,
    'kabab': 10,
    'morgh': 2,
    'sooshi': 7,
    'mahiche': 0,
    'pizaa(morgh)': 5,
    'pizaa(peperoni)': 8

}


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
        print('added ...')

def delet():
    show()

    name=input('enter name food :').lower()
    if name in resturan:
        del resturan[name]
        print('deleted ...')
    else :
        print('food mored nazar in resturan nist')
        
def sefaresh():
    show()

    print('--- menu resturan ---')
    show()
    n_food=input('enter name food :').lower()
    m_tedad=input('enter tedad mored nazar:')
    if n_food in resturan:
        if n_food >= m_tedad:
            resturan[n_food]=resturan[n_food]-m_tedad
            print('sefaresh sabt shode :) ')
        else :
            print('tedad mored nazar shoma mojood nist , soryy mojoodi :',resturan[n_food] ) 
    else :
        print('food mored nazar in resturan moojood nist')


def cancel_s():
    n_food=input('enter name food :').lower()
    m_food=input('enter tedad :')
    if n_food in resturan:
        resturan[n_food]=resturan[n_food]+m_food
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