seats = {
    "a1": "empty",
    "a2": "empty",
    "a3": "empty",
    "a4": "empty",
    "a5": "empty"
}
def show():
        for s , x in seats.items() :

            print( s, ':' , x )        
def Reserve():

    n_seats=input('enter name sit :').lower()
    if n_seats in seats :
        if seats[n_seats] == "empty" :
            n_karbar=input('enter name for reserv :').lower()
            seats[n_seats]=n_karbar
            print('rezerv with you _ thank you :)')
        else :

            print('sandali mored nazar rezev shode ast , sorry :( ')
    else :

        print('not found!!')

def cancel():

    n_sit=input('enter name sit :').lower()

    name=input('enter name please :').lower()

    if n_sit in seats:

        if seats[n_sit]=="empty" :

            print('in sit rezerv nist !! ')
        else :
            seats[n_sit]!="empty"
            print('rezer cancel shode bedrood :|')    

    else :
        print('your sit in sinema not found :')

def search_customer():
    name = input("Enter customer name: ")

    for seat, cus in seats.items():
        if cus == name:
            print(name, "sandali : ", seat)
while True:
    print("-----menu-----")
    print("\n1. Show seats")
    print("2. Reserve a seat")
    print("3. Cancel reservation")
    print("4. Search customer")
    print("5. Exit")

    m=int(input('enter number in menu:'))

    if m == 1 :

        show()

    elif m == 2 :

        Reserve()

    elif m == 3 :

        cancel()

    elif m == 4: 

        search_customer()

    elif m == 5 :

        print('good byee')
        break

    else:
        print('enter number in list ')