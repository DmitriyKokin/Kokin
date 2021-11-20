'''Первое приложение :'''
print ("Hello world!!!")
'''Домашняя работа 2 
Первое задание:'''
a = input('a =')
b = input('b =')
if a.isdigit() and b.isdigit():
    a = float(a)
    b = float(b)
    print(f'a+b = {a+b}')
    print(f"a-b = {a-b}")
    print(f"b-a ={b-a}")
    print(f"a*b ={a*b}")
    print(f"a/b ={a/b}")
    print(f"a^b ={a**b}")
    print(f"a%b ={a%b}")
    print(f"a//b ={a//b}")

else: print(f"enter digit!")

#Второе задание
yourname = input(f'what is your name?\n')
print (f"nice to meet you, {yourname}")
