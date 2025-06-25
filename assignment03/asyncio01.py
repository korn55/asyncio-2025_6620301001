# check the type of a coroutine
import asyncio
# define a coroutine
async def custom_coro():
    # await another conroutine
    await asyncio.sleep(1)

# create the coroutine
coro = custom_coro()
# check the type of a conroutine
print(type(coro))