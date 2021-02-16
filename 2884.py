a, b = input().split( )
a = int(a)
b = int(b)
b = b-45
if b < 0:
    b = b + 60
    a = a - 1
    if a < 0:
        a = a + 24
print(a,b)