anbar={
    'bag' : 100,
    'pen' : 20, 
    'pencie' : 40,
    'market' : 60
}


while True: 

    print('\n---------Menu---------')
    print(' 1 = add ')
    print(' 2 = show ')
    print(' 3 = exit ')

    a=int(input('\n enter number in list :'))

    if a==1 : 
        n=input('enter name kala : ')
        v=int(input('entr valiu kala :'))
        if n in anbar :
            anbar[n]=anbar[n]+v
            print( n , '\n ----> added')

        else :
            anbar[n]=v
            print( n , 'added')

    if a==2 :
        for a , b in anbar.items() :
            print( a, ':' , b )

    if a == 3 :
        print('\n good byy👌')
        break
       