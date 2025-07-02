# example of waiting for the first task to fail
from random import random
import asyncio

# corotine to execute in new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')
    # conditionnally fail
    if value < 0.1:
        raise Exception(f'Something bad happened in {arg}')
    
# main coroutine 
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for the first task to fail, or all tasks to complete
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    # report result
    print('Done')
    # get the first task to fail
    first = done.pop
    print(first)

# start the asyncio program
asyncio.run(main())
