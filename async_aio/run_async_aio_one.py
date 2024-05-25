import asyncio
import time


async def one():
    print("start one")
    await asyncio.sleep(1)
    print("stop one")


async def two():
    print("start two")
    await asyncio.sleep(2)
    print("stop two")


async def three():
    print("start three")
    await asyncio.sleep(3)
    print("stop three")


async def main():
    asyncio.create_task(one())
    asyncio.create_task(two())
    await asyncio.create_task(three())


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
