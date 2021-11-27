
print(f'enter a, b, c\n')
equation=['a','b','c']
for i in range(0,3):
    ask = input(f'{equation[i]} complex number? y/n\n')
    if ask == 'y' or ask == 'yes':
        print(f'{equation[i]} is complex')
        try:
            tmp = complex(int(input(f'RE = ')), int(input(f'IM = ')))
            equation[i] = tmp
        except:
            print('invalid enter')
            exit()
        print(equation)
    elif ask == 'no' or ask == 'n':
        try:
            equation[i] = float(input(f'{equation[i]}='))
        except:
             print('invalid enter')
             exit()
    else:
        print(f'be careful')
        exit()
#переходим к решению
d= pow(equation[1],2) - 4 * equation[0]*equation[2]
print(f'D = {d}')
if d == 0:
    try:
        print(f'd = 0\nx ={-equation[1]/2*equation[0]}')
    except ZeroDivisionError:
        print(f'Zero in denominator. a = 0.001')
        equation[0] = 0.001
        print(f'd = 0\nx ={-equation[1]/2*equation[0]}')
else:
    try:
        print(f'x1 = {(-equation[1] + pow(d,1/2))/(2*equation[0])}')
        print(f'x2 = {(-equation[1] - pow(d,1/2))/(2*equation[0])}')
    except ZeroDivisionError:
        print(f'Zero in denominator. a = 0.001')
        equation[0] = 0.001
        print(f'x1 = {(-equation[1] + pow(d,1/2))/(2*equation[0])}')
        print(f'x2 = {(-equation[1] - pow(d,1/2))/(2*equation[0])}')