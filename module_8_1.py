# a=123.456
# b = 'mystring'
def add_everything_up(a, b):
    try:
        c = (round((a+b), 3))
        print(c)
        # print(round((a + b), 3))
    except TypeError as typerr:
        # print(f'нельзя складывать данные разных типов: "{a}" и "{b}" -', typerr)
        c = str(a)+str(b)
        print(c)
    finally:
        print('='*12)
        # pass

def add_everything_mod(a, b):
    try:
        c = (round((a+b), 3))
        print(c)
        # print(round((a + b), 3))
    except TypeError as typerr:
        print(f'нельзя складывать данные разных типов: "{type(a)}: {a}" и "{type(b)}: {b}" -', typerr)
        c = str(a)+str(b)
        return c
    else:
        print(f'все прошло штатно, так как переменные {a} и {b} одного типа')
    finally:
        print('='*12)
        # pass

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
print('\n{txt:*^50}'.format(txt=' С пояcнением ошибок '))
add_everything_mod(123.456, 'строка')
add_everything_mod('яблоко', 4215)
add_everything_mod(123.456, 7)
