import asyncio
import random


async def say_after(delay: int, what):
    """Возвращает переданный объект с указанной задержкой delay"""
    await asyncio.sleep(delay)
    print(what)
    return what


async def say_after_failed(delay: int, what):
    """Копия say_after с ошибкой ZeroDivisionError"""
    1 / 0
    await asyncio.sleep(delay)
    print(what)
    return what


async def main():
    """Программа для запуска функций say_after и 1 функции say_after_failed,
    Идущей первой. Для сбора данных из корутин используется gather.
    При return_exceptions=True, ошибка не приводит к остановке выполнения
    программы. Возвращается объект ошибки. При return_exceptions=False ошибка
    приводит к вызову исключения и программа останавливается."""
    result = []
    tasks_pool = [say_after_failed(1, 1)]
    for i in range(100):
        task = asyncio.create_task(say_after(random.randint(1, 4), i))
        tasks_pool.append(task)
    result = await asyncio.gather(*tasks_pool, return_exceptions=True)
    return result


r = asyncio.run(main())
print(r)
print(type(r[0]))
