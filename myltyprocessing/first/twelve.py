import time
import threading
start = time.perf_counter()
def please_sleep(n):
    print("Sleeping for {} seconds".format(n))
    time.sleep(n)
    print("Done Sleeping for {} seconds".format(n))
threads = []
for i in range(1,10000):
    t = threading.Thread(target = please_sleep, args = [1])
    t.start()
    threads.append(t)
for t in threads:
    t.join()
finish = time.perf_counter()
print("Finished in {} seconds".format(finish-start))