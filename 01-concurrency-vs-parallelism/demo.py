import threading
import time


def task_a():
    for i in range(1, 4):
        print("A: ", i)
        time.sleep(0.1)

        
def task_b():
    for i in range(1, 4):
        print("B: ", i)
        time.sleep(0.1)


t1 = threading.Thread(target=task_a)
t2 = threading.Thread(target=task_b)
t1.start()
t2.start()
t1.join()
t2.join()