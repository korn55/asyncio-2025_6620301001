# example of running a coroutine
import asyncio
# define a coroutine
async def custom_coro():
    # await another coroutine  (sleep 1 วินาที)
    await asyncio.sleep(1)

# coroutine หลัก
async def main():
    # execute my  custom coroutine
    await custom_coro()

# start the coroutine program
asyncio.run(main())
