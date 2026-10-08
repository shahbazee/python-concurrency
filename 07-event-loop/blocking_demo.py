import asyncio
import time


async def good():
    print("Good start")
    await asyncio.sleep(1)
    print("Good Done")


async def bad():
    print("Bad start")
    time.sleep(1)
    print("Bad done")


async def main():
    start = time.time()
    await asyncio.gather(good(), bad())
    print("Time:", time.time() - start)


asyncio.run(main())