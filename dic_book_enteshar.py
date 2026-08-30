book={
    'java': 2020,
    'py': 2019,
    'html':2022
}
def show(): 
    for i , b in book.items() :
        print( i, ':' , b )
def add():
    d=input('entetr name book : ')
    r=input('enter sal enteshar your book  : ' )
    if d in book : 
        print(' have your book ')
    else:
        book[d]=r
        print(' adeded book ')
        show()
    
def serch():
    c= input('enter name book :')
    if c in book :
        print(book[c])
    else :
        print('not found your book , sorry ')

def delet() : 
    show()
    j=input('enter name book for delet: ')
    if j in book :
        del book[j]
        print('deleted ...')
    else:
        print('not found book !! checki again !!')
while True:
    print('1 ---> show ')
    print('2 ---> add')
    print('3 ---> serch ')
    print('4 ---> del')
    print('5 ---> exit')
    a = int(input('enter number menu: '))

    if a == 1:
        show()
    elif a == 2:
        add()
    elif a == 3:
        serch()
    elif a == 4 :
        delet()
    elif a == 5: 
        break
    else :
        print('please (1-4)')