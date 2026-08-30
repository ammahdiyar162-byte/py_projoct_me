books = [
("python", "ali", 3),
("c++", "reza", 2),
("java", "sara", 0)
]
def add():
    
    a=input('enter name book :').lower()
    b=input('enter name  talif konanade :').lower()
    c=input('enter noshke mojood :')
    y=(a, b , c)
    if y in books:
        print('your book in list_library !!!')
    else :
        books.append(y)
        print('added')

def show():
    print(books)

def serch():

    show()
    
    s=input('enter name book :').lower()
    d=input('enter talif  :').lower()
    for g in books:
        if g[0] == s.lower() and g[1] == d.lower():
            p=False
            print('\n---- found book ----')
            print(f'n_book : {g[0]}')
            print(f'talif  : {g[1]}')
            print(f'nosthe  : {g[2]}')
            p=True
        else :
            print('not found book !!')

    else :
        print('not found your book !!!')
        
def delet():

    show()

    t=input('enter name book:').lower()
    r=input('enter name talif  book:').lower()
    for n in books:
        if n[0].lower()==t.lower() and n[1].lower()==r.lower():
            books.remove(n)
            print('book removre')
        else :
            print('not founed')
    

def av() :
    pass
while True:
    print('------menu------')
    print("\n1. Add book")
    print("2. Show books")
    print("3. Search book")
    print("4. Delete book")
    print("5. Show available books")
    print("6. Exit")

    w=int(input('enter number in menu :'))
    if w == 1 :
        add()
    elif w == 2 :
        show()
    elif w == 3 :
        serch()
    elif w == 4 :
        delet()
    elif w == 5 :
        av()
    elif  w == 6 :
        print('Good Byee')
        break