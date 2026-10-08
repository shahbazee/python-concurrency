import asyncio


async def work(n, sem):
    async with sem:
        print("Start: ", n)
        await asyncio.sleep(1)
        print("Done: ", n)


async def main():
    sem = asyncio.Semaphore(2) 
    tasks = [work(i, sem) for i in range(1, 6)]
    await asyncio.gather(*tasks)


asyncio.run(main())