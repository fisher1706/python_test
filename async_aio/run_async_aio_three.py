import asyncio
import time
import aiohttp
import requests


async def blocking():
    resp = requests.get("https://google.com")
    print(resp.status_code)


async def async_http():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://google.com") as resp:
            print(resp.status)


async def main_one():
    await asyncio.gather(*(blocking() for _ in range(5)))


async def main_two():
    await asyncio.gather(*(async_http() for _ in range(5)))


if __name__ == '__main__':
    start = time.time()
    # asyncio.run(main_one())
    asyncio.run(main_two())
    end = time.time()
    print(end - start)
