import asyncio


async def mygen(u: int = 10):
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(1)


async def main():
    g = [i async for i in mygen(3)]
    f = [j async for j in mygen(3) if not (j // 3 % 5)]
    return g, f

g, f = asyncio.run(main())
print(g)
print(f)