import asyncio


async def fetch_data(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} done")
    return f"{name} data"


async def main():
    print("=== Direct await ===")
    result = await fetch_data("A", 1)
    print(f"Got: {result}\n")

    print("=== create_task ===")
    task = asyncio.create_task(fetch_data("B", 2))
    print("Task background mein, main aur kaam...")
    await asyncio.sleep(0.5)
    print("Ab result lo...")
    result = await task
    print(f"Got: {result}")


asyncio.run(main())
