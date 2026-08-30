mm= { 
    'name' : 'mahdiyar',
    'family' : 'headari',
    'age' :14,
    'major': 7 
}
print(mm)

print(mm['name'])
print(mm['family'])
print(mm['age'])
print(mm['major'])
#چاپ با get 
print('-----------------****----------------------------*****----------------------------****----------------------')

print(mm.get('name'))
print(mm.get('family'))
print(mm.get('age'))
print(mm.get('major'))

#اضفه کردن مقدار جدید 
print('----------------------------------------------------')

mm['avg'] = 20
print(mm)
#تعققیر یک کلید و مقدار 
print('-------------------------------------------------------')
#
mm['age']= 15
print(mm['age'])
#حذف و تعقییر کلید و مقدار 

del mm ['family']
print(mm)

mm={"family" : 'hhhh '}
print(mm['family'])
#چاپ مجدد  دوباره
print(mm)


x=mm.pop('name')
print('delted✌✌✌👌')
print(mm)

x= mm.popitem()
print(mm)

for k , v in mm.items() :
    print(k ,':', v)



print(mm.items())
print(mm.keys())
print(mm.values())





