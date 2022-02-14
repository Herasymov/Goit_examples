import asyncio

async def coro(seq) -> list:
    await asyncio.sleep(max(seq))
    return list(reversed(seq))

async def main():
    t = asyncio.create_task(coro([3, 2, 1]))
    await t
    print(f't: type {type(t)}')
    print(f't done: {t.done()}')

t = asyncio.run(main())