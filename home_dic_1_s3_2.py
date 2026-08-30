sh={
    'pen' : 20,
    'pencile' : 10,
    'book' : 50 , 
    'note book' : 2,
    'bag' : 0
}
x=input("enter name kala: ")
if x in sh :
    print('mojoodi kala :',sh[x])
a=sh[x]

if a == 0:
    print('namoojod!!!')

else :
    print(' not have item :')
