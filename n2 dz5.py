def summatr(*Args):
    s = 0
    for i in Args:
        s += i
    return s

print(f'{summatr(1,2)}')
print(f'{summatr(1,2,3)}')
print(f'{summatr(1,2,-4,0,4,3,6,4,3,5,6,4,6,53,535,-1000,5)}')
print(f'{summatr()}')