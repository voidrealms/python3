#IF ELSE ELIF
#Simple flow control

#If condition
x = False
if x:
    print('yes')
    print('again')
else:
    print('HELP!!!!!')
    
#Condition evaluations (True - run | False - not run)
x = 100
y = 25
if y == x: print('equal to')
if y != x: print('not equal to')
if y < x: print('less than')
if y > x: print('greater than')
if y <= x: print('less than or equal to')
if y >= x: print('greater than or equal to')

#Elif is the switch solution
x = 75
if x == 25:
    print('x = 25')
elif x == 50:
    print('x = 50')
elif x == 75:
    print('x = 75')
elif x == 100:
    print('x = 100')
else:
    print('catch all here')

#Nested statements
x = 82
if x > 50:
    print('over 50')
    if x > 60:
        print('over 60')
        if x > 70:
            print('over 70')
            if x > 80:
                print('over 80')
                if x > 90:
                    print('over 90')
                    if x >= 100:
                        print('complete')