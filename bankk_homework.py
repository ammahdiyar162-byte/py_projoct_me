bank={
    'ali':500000,
    'sara':800000,
    'reza':300000,
    'mina':1000000
}
def show_balance():
    
    for b,n in bank.items():
        print(f'Mr/mrs: {b}:{n}') 
def deposite():
    t=input('enter name please :')
    y=int(input(float('enter price for variz:')))
    if t in bank:
        bank[y]=bank[y]+y
    else :
        print('your name not have in bank (menu>>>>>5)')
def withdraw():
    a=input('enter name please :').lower()
    g=int(input(float('enter price for bardasht:')))   
    if a in bank:
        if bank[a]>=g:
            bank[g]=bank[g]+g
        else :
            print('not have moojodi :')
    else :
            print('not found your name in bank (menu>>>>5)')
        
def transfer():
    e=input('enter name please :')
    d=input('enter name fard morede nazar')
    p=int(input(float('enter price for bardasht:')))
    if e in bank :
        if d in bank:
            bank[e]=bank[e]-p
            bank[d]=bank[d]+p
        else : 
            print('fard mored nazar dar bank nist')
    else :
        print('not found tour name ... ')
        

def add_cus():
    n=input('enter name  : ')
    v=int(input('entr mojoodi :'))
    if n in bank :
            bank[n]=v
            print( n , '\n ----> added')
while True:
    print('1--> show moojodi')
    print('2--> variz vajhe ')
    print('3--> bardasht vajh')
    print('4-->enteghal vajhe  ')
    print('5--> add karbar in bank ')
    print('6--> exit bank ')

    l=int(input('enter number menu'))
    if  l== 1 :
        show_balance()
    if l== 2 :
        deposite()
    if l== 3 :
        withdraw()
    if l== 4 :
        transfer()
    if l== 5 :
        add_cus()
    if l== 6 :
         break