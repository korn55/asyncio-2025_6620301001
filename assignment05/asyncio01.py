# example of waiting for all tasks to complete
from random import random
import asyncio 

# coroutine to  execute in new task 
async def task_coro(arg):
    # generate a random value between 0 and 1 
    value  = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')

    # main corotine 
    async def main():
        # create many tasks
        task = [asyncio.create_task(task_coro(i)) for i in range(10)]
        # wait for all task to complete
        # done,pending = awit asyncio.wait(task,return_when=asycio.ALL_COMPLETED)
        done,pending = await asyncio.wait(task)
        # report results
        print('All done')

    # start the asyncio program
    asyncio.run(main())