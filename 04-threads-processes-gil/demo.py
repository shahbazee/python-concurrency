import threading
import multiprocessing
import time


def cpu_work(n):
    count = 0
    for i in range(5_000_000):
        count += i
    return count


if __name__ == "__main__":
    start = time.time()
    cpu_work(1)
    cpu_work(2)
    print(f"Sequential: {time.time() - start:.1f}s")

    start = time.time()
    t1 = threading.Thread(target=cpu_work, args=(1,))
    t2 = threading.Thread(target=cpu_work, args=(2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Threads: {time.time() - start:.1f}s")

    start = time.time()
    p1 = multiprocessing.Process(target=cpu_work, args=(1,))
    p2 = multiprocessing.Process(target=cpu_work, args=(2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Processes: {time.time() - start:.1f}s")
