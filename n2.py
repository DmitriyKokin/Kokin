import random
#Создание словаря из цветов:
color = dict([('red',(1,0,0)), ('black', (0,0,0)), ('white',(1,1,1)), ('blue', (0,0,1))])
print(f'{color}')
#cоздание 2-х множеств
try:
    n = int(input(f'Введите количество ранодомных значений, которые сгенерируются, с учетом дублей\n'))
except:
    print(f'User error')
a=set()
for i in range(0,n):
    tmp = random.randint(1,10)
    a.add(tmp)
try:
    n = int(input(f'Введите количество ранодомных значений, которые сгенерируются, с учетом дублей во второе множество\n'))
except:
    print(f'User error')
b=set()
for i in range(0,n):
    tmp = random.randint(1,10)
    b.add(tmp)
print(f'Первое множество:{a}\nВторое множество: {b}')
#входят одновременно в оба;
print(f'входят одновременно в оба {set.intersection(a,b)}')
#входят в 1 и не входят во 2

print(f'входят в 1 и не входят во 2: {a.difference(b)}')
#входят во 2 и не входят в 1
print(f'входят во 2 и не входят в 1: {b.difference(a)}')
#входят в первое или во второе, но не в оба из них одновременно
print(f'входят в первое или во второе, но не в оба из них одновременно: {a.difference(b).union(b.difference(a))}')
