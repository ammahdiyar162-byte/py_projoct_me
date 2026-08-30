#اسمی با شماره 
c={
    'ali': 8548,
    'amir' : 5718,
    'mahdi' : 8181,
    'ariyan' : 4582
}
#گرفتن وردی از کاربر 
x=input('enter name :')
if x in c :
#چک کردن و چاپ شماره وارد شده توسط کاربر در  INput
    print('phone :', c[x])
else :
    print('invalid!!! check name and startt 2 agine')