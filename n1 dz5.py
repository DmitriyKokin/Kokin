def passwd(pas):
    """Функция получает на входе строку, предполагаемый пароль
       проверяет строку на соответствие длинны, наличие цифр, букв
       отстутствие подстроки password в любом регистре
       при прохождении всех проверок, возвращается True, иначе - False
       """   
    if len(pas) < 6:
        return False
    ch = True
    ch1 = True
    for i in pas:
        if i.isdigit():
            ch = False
        else:
            ch1 = False
    if ch or ch1:
        return False
    lasttest = pas
    lasttest = lasttest.lower()
    if lasttest.find('password') == -1:
        return True
    else:
        return False
print(f"{passwd(input(f'Enter password .. '))}")
