import asyncio
import time


async def task_a():
    await asyncio.sleep(1)
    return "A done"


async def task_b():
    await asyncio.sleep(3)
    return "B done"


async def task_c():
    await asyncio.sleep(5)
    return "C done"


async def main():
    start = time.time()
    results = await asyncio.gather(task_a(), task_b(), task_c())

    print(results)
    print("Time:", time.time() - start)


asyncio.run(main())