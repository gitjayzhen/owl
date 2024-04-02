# -*- coding:utf-8 -*-

"""
@author:    jayzhen
@file:      test_gather
@time:      2020-12-25 15:42
"""


import asyncio


async def add(f, i):
    f += i
    return f


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        # print(f"Task {name}: Compute factorial({i})...")
        f = await add(f, i)
        # f += i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 200000),
        factorial("B", 300000),
        factorial("C", 400000),
    )

if __name__ == '__main__':
    import time
    # 0.00621485710144043
    # 0.02331399917602539
    a = time.time()
    asyncio.run(main())
    print(time.time() - a)
