import threading
import time


def fetch(n):
    time.sleep(1)
    print("Fetched:", n)


start = time.time()
for i in range(1, 4):
    fetch(i)
print("Sequencial:", time.time() - start)


start = time.time()
threads = []
for i in range(1, 4):
    t = threading.Thread(target=fetch, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Threaded: ", time.time() - start)