try:
    maxmass=int(input(f'Введите максимально возможную массу для инвентаря (целое число):\n'))
except:
    print(f'UserError')
    exit()
invent = 0
a = dict()
tmp = True
while invent <=maxmass:
    c = input(f'Введите команду (добавить, удалить, выход))\n')
    if c == 'добавить' or c== 'удалить' or c=='выход':
        if c == 'добавить':
            tmp = input(f'название: ')
            tmp1 = int(input(f'вес: '))
            invent+=tmp1
            a[tmp] = tmp1
            print(f'сейчас в инвентаре: {a}, масса составляет {invent} ')
        elif c == 'удалить':
            try:
                tmp = input(f'название: ')
                invent=invent-a.get(tmp)
                del a[tmp]
                print(f'осталось это: {a}, масса {invent} ')
            except:
                print(f'UserError')
                exit()
        elif c == 'выход':
            print(f'содержимое {a} пропало')
            exit()
        else:
            print(f'UserError')
            exit()
    