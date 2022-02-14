import time
import threading


def please_sleep(n):
    print("Sleeping for {} seconds".format(n))
    time.sleep(n)
    print("Done Sleeping for {} seconds".format(n))


start = time.perf_counter()
print(start)
threads = []
for i in range(1, 5):
    t = threading.Thread(target=please_sleep, args=[i])
    t.start()
    threads.append(t)
for t in threads:
    t.join()
finish = time.perf_counter()
print("Finished in {} seconds".format(finish-start))
