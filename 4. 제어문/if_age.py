x = int(input("Please enter your age: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x > 0 and x < 20:
    print('Young')
elif x >= 20 and x < 30:
    print('Still Young')
else:
    print('Old')