bank={
    'ali' : 2000000,
    'mahdi':500,
    'amir':800000,
    'sadra':500000,
}
def show():
    a=input('enter your name :')
    if a in bank:
        pirnt(bank[a])
    else :
        print('not have your name check again and can (menu>>>6)')
def showall():
    pas='123456'
    a=input('enter number password')
    if a == pas:
        print('welcome modir '[bank])
    else:
        print('password invalid please check!!! ')
    






print('----------menu bank --------------')
while True:
    print('1 ---> show moojoodi :')
    print('2 ---> show all mojodi (for modir) :')
    print('3 ---> show mojoodi :')
    print('4 ---> bardasht moojodi:')
    print('5 ---> afzaesh mojiodi :')
    print('6 ---> add hesab  :')
    print('7 ---> del hesab  :')
    print('8 ---> exit bank  :')

    i=int(input('enter number in menu :'))
    
    if i == 1 :
        show()
    if i == 2:
        showall()
    if i == 3:
        pass 

    if i == 4:
        bardasht()
    if i == 5:
        afzaesh()
    if i == 6:
        add(1)
    if i == 7:
        delet()
    if i == 8 :
        break