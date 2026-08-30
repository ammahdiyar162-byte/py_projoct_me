# لیست اولیه شما
my_list = ['book', 'note book', 'pen']

while True:
    print("\n--- Menu ---")
    print("1 - Add")
    print("2 - Show")
    print("3 - Delete")
    print("4 - Exit")
    
    # گرفتن ورودی از کاربر
    x = int(input('Enter number (1-4): '))

    if x == 1:
        # گزینه ۱: اضافه کردن آیتم جدید
        item = input('Enter the item to add: ')
        my_list.append(item)
        print("Item added!")

    elif x == 2:
        # گزینه ۲: نمایش لیست
        print("Current List:", my_list)

    elif x == 3:
        # گزینه ۳: حذف کلمه
        item_to_remove = input('Enter the item to delete: ')
        
        # چک می‌کنیم که آیا کلمه در لیست هست یا نه تا برنامه خطا ندهد
        if item_to_remove in my_list:
            my_list.remove(item_to_remove)
            print("Item removed!")
        else:
            print("This item is not in the list.")

    elif x == 4:
        # گزینه ۴: خروج
        print("Goodbye!")
        break
    
    else:
        # اگر عدد بین ۱ تا ۴ نباشد
        print("Please enter 1, 2, 3, or 4.")
