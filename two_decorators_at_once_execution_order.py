def dec_i_can(func):
    print('dec_i_can at work')
    def wrapper():
        print('Кто умеет писать декораторы?')
        who_am_i = func()
        print(f'{who_am_i=}')
    print('dec_i_can returned wrapper')
    return wrapper

def one_more_dec(func):
    print('one_more_dec at work')
    def wrapper():
        print("Я умею писать декораторы")
        print(f"{func=}")
        return func()
    print('one_more_dec returned wrapper')
    return wrapper


@dec_i_can
@one_more_dec
def f():
    print("И кто я тогда?")
    return "Красава"

print('func start')
f()
# Результат вывода:
# one_more_dec at work
# one_more_dec returned wrapper
# dec_i_can at work
# dec_i_can returned wrapper
# func start
# Кто умеет писать декораторы?
# Я умею писать декораторы
# func=<function f at 0x7facf615e050>
# И кто я тогда?
# who_am_i='Красава'