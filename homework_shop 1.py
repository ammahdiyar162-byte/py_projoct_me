name = []
price = []

while True:
    print("1 - Add")
    print("2 - See list")
    print("3 - Delete")
    print("4 - Exit")
    print("5 - add price!")

    a = int(input("Enter your number :: "))
    # b = int(input('enter price:'))

    if a == 1:
        name = input("Enter item name: ")
        nam.append(name)

        print("OK! Added to the list.")

    elif a == 2:
        print("seee List:")

        for item in nam:
            print(item)

    elif a == 3:
        name = input("Enter item foor delete: ")

        if name in nam:
            nam.remove(name)
            print("Deleted!")
        else:
            print("Item not found !!!!!!.")

    elif a == 4:
        print("Goooooood day :) !")
        break
        

    else:
        print("Invalid please  chekkkkk!  :_(")