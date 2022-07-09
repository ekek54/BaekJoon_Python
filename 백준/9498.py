# 9498 https://www.acmicpc.net/problem/9498
a= input()
a = int(a)
if 100 >= a and a >= 90:
    print('A')
elif 90 > a and a >= 80:
    print('B')
elif 80 > a and a >= 70:
    print('C')
elif 70 > a and a >= 60:
    print('D')
elif 60 > a:
    print('F')