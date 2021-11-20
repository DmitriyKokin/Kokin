'''ТЕСТОВЫЙ ФАЙЛИК С ПРОВЕРКОЙ КОМАНД'''
import math
import random
var1 = int(input("var1 = "))
var2 = int(input("var2 = "))
#битовые операции
print (f'{var1 | var2}')
print (f'{var1 ^ var2}')
print (f'{var1 & var2}')
print (f'{var1 << var2}')
print (f'{var1 >> var2}')
print (f'{~var2}')
#тесты на системы счисления
x = int(input("X = "))
x = bin(x)
print(f'_2  {x}')
x = int(input("X = "))
x = oct(x)
print(f'_8 {x}')
x = int(input("X = "))
x = hex(x)
print(f'_16 {x}')
x = int(x, 16)
print(f'_10 {x}')
#использование подключенных модулей
print(f"pi {math.pi}\n sqrt(25) {math.sqrt(25)}\n random1-10 {random.randint(1,10)}")




