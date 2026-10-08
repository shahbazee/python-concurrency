import asyncio
import time


def get_user_from_db(user_id):
    time.sleep(2)
    return f"user {user_id}"

    
async def main():
    start = time.time()
    users = await asyncio.gather(
        asyncio.to_thread(get_user_from_db, 1),
        asyncio.to_thread(get_user_from_db, 2),
        asyncio.to_thread(get_user_from_db, 3),
    )
    print(users)
    print("Time: ", time.time() - start)


asyncio.run(main())