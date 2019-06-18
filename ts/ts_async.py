#!/usr/bin/python
# coding:utf-8
# author dongguanghua

"""
# import asyncio
# import time
# import concurrent.futures
#
# IoLoop = asyncio.get_event_loop()
#
#
# async def mySleep(n):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
#         futures = [IoLoop.run_in_executor(executor, time.sleep, n)]
#         await asyncio.wait(futures)  # or
#         # return [ret for ret in await asyncio.gather(*futures)]
#
#
# async def do_work1():
#     await mySleep(5)
#     print("doWork1")
#
#
# async def do_work2():
#     await mySleep(5)
#     print("doWork2")
#
#
# if __name__ == "__main__":
#
#     task = [do_work1(), do_work2()]
#     IoLoop.run_until_complete(asyncio.gather(*task))
"""


import asyncio


async def wget(host):
    print('wget %s...' % host)
    reader, writer = await asyncio.open_connection(host, 80)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    # send
    writer.write(header.encode('utf-8'))
    await writer.drain()

    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()

tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
