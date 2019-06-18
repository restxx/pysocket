# coding=utf8
# __author__ = 'doc007'

import time
import sys
import asyncio
from functools import wraps
# import concurrent.futures


def excepts(info):
    def dec(func):
        @wraps(func)
        def warp(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as err:
                print("[%s], funcName=[%s], error=[%s][%s]" % (str(self.__class__), func.__name__, info, str(err)))
                return -1

        return warp

    return dec


get_running_loop = asyncio.get_running_loop if sys.version_info >= (3, 7) else getattr(asyncio, '_get_running_loop')


def coroutine(ioLoop=None):
    def dec(func):
        @wraps(func)
        async def warp(*args):
            """
            # with concurrent.futures.ThreadPoolExecutor() as executor:
            #     futures = [ioLoop.run_in_executor(executor, func, *args, **kwargs)]
            #     await asyncio.wait(futures)
            #     ------or-------------------------
            #     # _ = [ret for ret in await asyncio.gather(*futures)]
            # ------------------------ or--------------------------------
            # futures = [ioLoop.run_in_executor(None, func, *args, **kwargs)]
            # await asyncio.wait(futures)
            """
            Ioloop = get_running_loop() if ioLoop is None else ioLoop
            await asyncio.gather(Ioloop.run_in_executor(None, func, *args))

        return warp

    return dec


#   -------------------------------------------------
class a(object):
    @excepts("aaaaaa")
    def ts(self, a, b):
        print(a, b)
        raise Exception("ab error")


@coroutine(None)
def mySleep(n):
    return time.sleep(n)


async def do_work(n):
    await mySleep(n)
    print("do_work1")


async def do_work2(n):
    await mySleep(n)
    print("do_work2")


if __name__ == '__main__':
    IoLoop = asyncio.get_event_loop()
    IoLoop.run_until_complete(asyncio.wait([do_work(5), do_work2(5)]))
    IoLoop.close()

    # a().ts(1, 3)
    pass
