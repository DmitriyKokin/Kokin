#Строки, их функции и методы
str = "Hello world"
str = str + '!!!'
print(f'{str}')
print(f'{str}\r')
print(f'{str}\n')
S = b'byte'
S1  = 'My first'
print(f'{S1}\n')
S2 =  S1 +' '+ str
print(f'{S2}')
print(f'{S1} {str}')
print(f'{S2[3:]}')
print(f'{S2.find(S1,0,10)}')
print(f'{S2.find(str)}')
# Replace - Замена подстроки на другую подстроку
SS = 'London is the capital of Great Britain'
SS = SS.replace('is the', 'IS THE')
print(f'{SS}')
SS = 'London is the capital of Great Britain'
SS = SS.split('o')
print(f'{SS}')
SS = 'London is the capital of Great Britain'
a = SS.istitle()
print(f'{a}')
print(f'{SS.startswith("Lond")}')
SS = 'London\nis\nthe\ncapital\nof Great\nBritain\n'
SS = SS.capitalize()
SS = SS.center(31)
SS = SS.upper()
print(f'{SS}')
print(f'{ord("S")}')
print(f'{SS}')