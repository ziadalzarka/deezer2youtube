import random
import asyncio


async def dostuff(stuff):
    t = random.randint(1, 5)
    await asyncio.sleep(t)
    print(str(t) + stuff)


async def main():
    task1 = asyncio.create_task(dostuff("task1"))
    task2 = asyncio.create_task(dostuff("task2"))
    task3 = asyncio.create_task(dostuff("task3"))

    await task1
    await task2
    await task3

    print("complete")

asyncio.run(main())
