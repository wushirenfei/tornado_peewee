# -*- coding=utf-8 -*-

"""
:author alex
:date 2018/3/9 

"""
import time
import random
import asyncio


@asyncio.coroutine
def yield_fib(n):
    start = time.time()
    a, b, index, sum_sleep = 0, 1, 0, 0
    while index < n:
        sleep_secs = random.uniform(0, 0.5)
        sum_sleep += sleep_secs
        yield from asyncio.sleep(sleep_secs)
        print('yield_fib think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
    print('using: {} sec, sleep: {} sec'.format(time.time() - start, sum_sleep))


async def async_fib(n):
    start = time.time()
    a, b, index, sum_sleep = 0, 1, 0, 0
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        sum_sleep += sleep_secs
        await asyncio.sleep(sleep_secs)
        print('async_fib think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
    print('using: {} sec, sleep: {} sec'.format(time.time() - start, sum_sleep))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(yield_fib(10)),
        asyncio.ensure_future(async_fib(10))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
