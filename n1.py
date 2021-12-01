try:
    n = int(input(f'Введите n - количество элементов в массиве:\n'))
except :
    print(f'USER ERROR')
    exit()
a=[]
try:
    for i in range(0,n):
        a.append(float(input(f'{i}-й элемент: ')))
except:
    print(f'USER ERROR')
    exit()
print(f'Наш массив:{a}')
try:
    ch = int(input(f'min -> max ---- 1\nmax -> min ---- 2\n'))
except:
    print(f'USER ERROR')
    exit()
#Реализация метода пузырька:
for i in range(0,n):
    for j in range(n-i-1):
        if a[j]>a[j+1] and ch == 1:
            a[j],a[j+1]=a[j+1],a[j]
        elif a[j]<a[j+1] and ch == 2:
            a[j],a[j+1]=a[j+1],a[j]
print(f'отсортированный массив: {a}')