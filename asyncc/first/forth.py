import asyncio
import time


async def execute(delay, value):
    await asyncio.sleep(delay)
    print(value)


async def main():
    try:
        await asyncio.wait_for(execute(1, "Hello"), 2)
    except:
        print("Time out")

asyncio.run(main())
