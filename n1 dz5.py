def passwd(pas):
    #проверка на длину пароля
    if len(pas) < 6:
        return False
    #проверка на содержание цифры и отсутствия только цифр
    ch = True
    ch1 = True
    for i in pas:
        try:
            tmp = int(i)
            ch = False
        except ValueError:
            ch1 = False
            pass
    if ch or ch1:
        return False
    #проверка на password
    lasttest = pas
    lasttest = lasttest.lower()
    if lasttest.find('password') == -1:
        return True
    else:
        return False

print(f"{passwd(input(f'Enter password .. '))}")