student = [
("Ali", "Ahmadi", 16, 14.5),
("sadra", "Mohammadi", 11, 20),
("amir", "Karimi", 17, 11.75),
("mahdi", "Hosseini", 16, 9)
]

def add():
    a=input('enter name please:')
    b=input('enter last name please:')
    c=int(input('enter birstday please :'))
    d=int(input('enter moadel please:'))
    y=(a,b,c,d)
    student.append(y)
    print('student added  :)')



def show():
    print(student)



def serch():
    s=input('enter name please :')
    d=input('enter last name please :')
    for g in student:
        if g[0] == s.lower() and g[1] == d.lower():
            print('\n---- found student ----')
            print(f'name : {g[0]}')
            print(f'family : {g[1]}')
            print(f'age : {g[2]}')
            print(f'moadel : {g[3]}\n')
        else :
            print('not found student !!')

def delet():
    t=input('enter name please:')
    r=input('enter family please:')
    for n in student:
        if n[0].lower()==t.lower() and n[1].lower()==r.lower():
            student.remove(n)
            print('student removre')
        else :
            print('not founed')
    return

def moadel():
    pass

def pas_fail():
    passed = 0
    failed = 0
    
    for s in student:
        if s[3] >= 10:
            passed += 1
        else:
            failed += 1
            
    print(f'\nPassed students: {passed}')
    print(f'Failed students: {failed}\n')
while True:
    print('--------> menu <--------')
    print('1... Add student')
    print('2... Show students')
    print('3... Search student')
    print('4... Delete student')
    print('5... Show class average')
    print('6... Show passed and failed')
    print('7... Exit')
    m=int(input('enter number in menu:'))
    if m == 1:
        add()
    if m == 2:
        show()
    if m == 3 :
        serch()
    if m == 4 :
        delet()
    if m == 5 :
        moadel()
    if m == 6 :
        pas_fail()
    if m == 7 :
        break


    else :
        print('enter in menu')