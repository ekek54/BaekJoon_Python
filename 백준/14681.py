a = input()
a = int(a)
b = input()
b = int(b)
if  a > 0 and b > 0:
    print('1')
elif  a < 0 and b > 0:
    print('2')
elif  a < 0 and b < 0:
    print('3')
elif  a > 0 and b < 0:
    print('4')