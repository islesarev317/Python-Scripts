import asyncio
import time

async def say_after(delay, what):
    print("started:", what)
    await asyncio.sleep(delay)
    print("ended:", what)


async def main():
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )

if __name__ == "__main__":
    print(f"started at {time.strftime('%X')}")
    asyncio.run(main())
    print(f"finished at {time.strftime('%X')}")
