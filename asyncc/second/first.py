import asyncio
import types


async def stuff():
    print("Hello ...")
    await asyncio.sleep(1)
    print("World!")


@types.coroutine
def py34_coro():
    """Generator-based coroutine, older syntax"""
    yield from stuff()


async def py35_coro():
    """Native coroutine, modern syntax"""
    await stuff()



asyncio.run(py34_coro())