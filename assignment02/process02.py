# Multiprocessing 2 kitchens, 2 cookers, 2 dishes
# Thread version of cooking 1 kitchen 1 chefs 1 dishes
import os
from time import time, ctime, sleep
import threading

def cooking(index):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...PID {os.getpid()}')
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index} : Begin cooking...')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} seconds!')

if __name__ == "__main__":
    # Begin of main thread
    print(f'{ctime()} Main      : Starting cook.')
    print(f'{ctime()} Main      : ID of main process: {os.getpid()}')
    start_time = time()
    
    # Multi thread cooking
    chefs = list()
    for index in range(5):
        c = threading.Thread(target=cooking, args=(index,))
        chefs.append(c)
        c.start()
    
    for index, c in enumerate(chefs):
        c.join()
    
    duration = time() - start_time
    print(f"{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds")