import asyncio


async def slow():
    await asyncio.sleep(5)
    return "Hogya"


async def main():
    try:
        result = await asyncio.wait_for(slow(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Time Khatam, kaam cancel")


asyncio.run(main())