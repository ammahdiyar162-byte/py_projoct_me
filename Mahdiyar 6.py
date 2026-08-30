
name=["mahdi", "ali", "amir", "amir"]
age=[12 , 13 , 14 , 12]
print('name:' ,name)
print('age:', age)
# append
name.append('Mashdiyar')
age.append(15)
print('name after append:',name)
print('age after append:',age)
#pop
name.pop()
age.pop()
print('name after pop:',name)
print('age after pop:',age)

name.remove("amir")
age.remove(14)

print('name after remove:',name)
print('age after remove:',age)



print('name after count:',name.count('amir'))
print('age after count:',name.count(12))




print('name after index:',name.index('mahdi'))
print('age after index:',age.index(13))

name.sort()
age.sort()

print('name after sort:',name)
print('age after sort:',age)

name.reverse()
age.reverse()

print('name after reverse:',name)
print('age after reverse:',age)