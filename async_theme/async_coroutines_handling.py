

import asyncio

async def f():
    print('running f')
    n = 2
    await asyncio.sleep(n)
    return n

async def g():
    print('running g')
    n = 3
    await asyncio.sleep(n)
    return n

async def fail():
    print('running fail')
    raise Exception("Ooops")


async def sequential_execution():
    """Запускает функции друг за другом"""
    print('running sequential_execution')
    result_f = await f()
    result_g = await g()
    print(f'{result_f=}, {result_g=}')


async def make_tasks_await_by_hand():
    """Запускаем функции конкурентно через таски вручную указав их ожидание"""
    print('running make_tasks_await_by_hand')
    task_f = asyncio.create_task(f())
    task_g = asyncio.create_task(g())
    result_f = await task_f
    result_g = await task_g
    print(f'{result_f=}, {result_g=}')

async def make_tasks_await_by_gather():
    """Запускаем функции конкурентно через gather"""
    print('running make_tasks_await_by_gather')
    result_f, result_g, result_fail = await asyncio.gather(f(), g(), fail(), return_exceptions=True)
    print(f'{result_f=}, {result_g=}, {result_fail=}')


async def wait_for_example():
    """Как работает wait_for. Добавляется таймаут для ожидания выполнения таски"""
    print('running wait_for_example')

    try:
        result_f, result_g, result_fail = await asyncio.wait_for(
            asyncio.gather(f(), g(), fail()),
            timeout=1.0,
        )
    except asyncio.TimeoutError:
        print("oops took longer than 1s!")
    except Exception:
        print("ouch")

    try:
        result_f = await asyncio.wait_for(f(),
            timeout=1.0,
        )
    except asyncio.TimeoutError:
        print("oops took longer than 1s!")


async def as_completed_usage():
    """Как работает as_completed"""
    print('running as_completed_usage')
    task_f = asyncio.create_task(f())
    task_g = asyncio.create_task(g())
    task_fail = asyncio.create_task(fail())

    for fut in asyncio.as_completed([task_f, task_g, task_fail], timeout=5.0):
        try:
            res = await fut
            print(res)
            print("one task down!")
        except Exception:
            print("ouch")


async def wait_usage():
    """Как работает wait. Wait будут убирать в 3.11"""
    print('running wait_usage')
    task_f = asyncio.create_task(f())
    task_g = asyncio.create_task(g())
    task_fail = asyncio.create_task(fail())
    done, pending = await asyncio.wait([task_f, task_g, task_fail], timeout=1, return_when=asyncio.FIRST_COMPLETED)
    print("going to done")
    for t in done:
        print(t)
        print(pending)
        try:
            res = await t
            print(res)
        except Exception as e:
            print(f"failed with { repr(e) }.")


if __name__ == '__main__':
    # asyncio.run(sequential_execution())
    # asyncio.run(make_tasks_await_by_hand())
    # asyncio.run(make_tasks_await_by_gather())
    # asyncio.run(wait_for_example())
    asyncio.run(as_completed_usage())
    # asyncio.run(wait_usage())


