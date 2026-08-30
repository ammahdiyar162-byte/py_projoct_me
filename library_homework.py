library={
    "Python": 30,
    "Java": 20,
    "C++": 5,
    "HTML": 6
}     # ساخت حلقه بی نهایت و لیت نمایش و گرفتن وردی از کاربر 
def show():
      for s,d in library.items() : 
                print( s , ':' , d)
def serch():
            e=input('enter name your book:')
            if e in library :
            
                print(e,':',library[e])
            else :
                print('not have your book')
def amanat():
        l=input('enter name i6tem for amanat : ')
        if l in library:
            if library[l] >0:
                library[l]=library[l] -1
                print(f'{l}  amanat dade shod ')
            else :
                print(' ama ketab dar amanat ast') 
        else:
            print('This Book Not Exist')
def back():
        m=input('enter name book for back  :')
        if m in library:
            library[m]=library[m] +1
            print('\n <3 back book thank you :)')
        else :
            print('not have your book for back in library please cheadk the book name !!!!!!!!!!!')
def add():
        v=input('enter name book :')
        b=int(input('enter mojoodi book :'))
        if v in library:
            library[v]=library[v]+b 
            print('\n add only moojodi chon kala moojod bood nosthe ha update shod !!') 
        else :
            library[v]=b
            print(f'{v} added')
     
while True :

    print('\n ----------modiriat-library-----------')
    print(' 1---> show books')
    print(' 2---> serche books')
    print(' 3---> amanat books')
    print(' 4---> back book to the library ')
    print(' 5---> add new book')
    print(' 6---> exit ')

    a=int(input('\n enter number in menu :'))

    if a == 1 :
      show()
    if a == 2 :
        serch()
    if a == 3 :
        amanat()
    if a== 4:
        back()

    if a == 5 :
        add()
    if a == 6 :
        print('good byeee')
        break
        