import asyncio


async def slow_work():
    await asyncio.sleep(2)
    return "kam hogyaa"


async def main():
    task = asyncio.create_task(slow_work())
    print("Task shuru ma or kam karta ho")
    await asyncio.sleep(0.5)
    print("Mera kam ho gaya, ab task ka intezar")
    result = await task
    print(result)


asyncio.run(main())