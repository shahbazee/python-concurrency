import asyncio
import time


def blocking_task(n):
    print(f"Blocking {n} start")
    time.sleep(2)
    print(f"Blocking {n} done")


async def non_blocking(n):
    print(f"Non blocking {n} start")
    await asyncio.sleep(2)
    print(f"NonBlocking {n} done")


async def main():
    print("===Blocking====")
    start = time.time()
    blocking_task(1)
    blocking_task(2)
    print(f"Time {time.time() - start:.1f}s\n")

    print("===Non Blocking===")
    start = time.time()
    await asyncio.gather(
        non_blocking(1),
        non_blocking(2),
    )
    print(f"Time: {time.time() - start:.1f}s")


asyncio.run(main())
