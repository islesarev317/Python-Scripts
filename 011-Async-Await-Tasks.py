import asyncio


async def hello(i):
    print(f">> hello {i} started")
    await asyncio.sleep(4)
    print(f">> hello {i} done")


async def main():
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))
    print("-- Start double sleep(3) --")
    await asyncio.sleep(3)
    print("-- End first sleep(3) --")
    await asyncio.sleep(3)
    print("-- End second sleep(3) --")
    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main())
