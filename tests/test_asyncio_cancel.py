# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@file:      asyncio_cancel.py
@time:      2020-08-07 15:37
"""

import asyncio
import time

COUNT = 0


async def do_some_work(x):
    global COUNT
    while True:
        print('Hello do_some_work:', asyncio.current_task().get_name())
        try:
            COUNT = COUNT + 1
            await asyncio.sleep(x)
        except asyncio.CancelledError:
            print('task do_some_work({}) was canceled'.format(x))
            raise  # 这里不raise的话，程序会继续，task 仍然是active(这是try, except特征决定的)
        print('do_some_work({}) is still active'.format(x))  # 如果这句话被打印，证明task仍是active
        # return "work is done for {}".format(x)


def cancel_task(future):
    future.cancel()
    print('cancelled the task:', id(future))


async def main(loop):
    tasks = []
    for i in range(5):
        print(i)
        coroutine = do_some_work(i)
        # task = asyncio.ensure_future(coroutine)
        task = loop.create_task(coroutine, name="a-{}".format(i))
        tasks.append(task)
        # loop.call_soon(cancel_task, task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    print('start...')
    start = time.time()
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    try:
        results = event_loop.run_until_complete(main(event_loop))
        for result in results:
            print("task result:", result)
    except KeyboardInterrupt:
        now = event_loop.time()
        # print(asyncio.Task.all_tasks())
        for task in asyncio.Task.all_tasks():
            print('cancelling the task {}: {}'.format(id(task), task.cancel()))
            # event_loop.call_soon(cancel_task, task)
        event_loop.stop()
        event_loop.run_forever()  # restart loop
    finally:
        event_loop.close()
    print(COUNT)
    end = time.time()
    print("total run time: ", end - start)
