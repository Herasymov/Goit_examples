import asyncio
import time


async def coro(seq) -> list:
    print(f"{max(seq)} before sleep")
    await asyncio.sleep(max(seq))
    print(f"{max(seq)} after sleep")
    return list(reversed(seq))


async def main():
    t = asyncio.create_task(coro([3, 6, 1]))
    t2 = asyncio.create_task(coro([1, 5, 0]))  # Python 3.7+
    print('Start:', time.strftime('%X'))
    a = asyncio.gather(t, t2)
    print("Before")
    res = a
    print('End:', time.strftime('%X'))  # Should be 10 seconds
    print(f'Both tasks done: {all((t.done(), t2.done()))}')
    return res

a = asyncio.run(main())
print(a)