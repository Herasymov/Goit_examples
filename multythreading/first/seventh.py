import time
import threading


def please_sleep(n):
    print("Sleeping for {} seconds".format(n))
    time.sleep(n)
    print(f"{n} Done Sleeping")


start = time.perf_counter()
t1 = threading.Thread(target = please_sleep, args = [1])
t2 = threading.Thread(target = please_sleep, args = [2])
t3 = threading.Thread(target = please_sleep, args = [3])
t4 = threading.Thread(target = please_sleep, args = [4])
t5 = threading.Thread(target = please_sleep, args = [5])
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
finish = time.perf_counter()
print("Finished in {} seconds".format(finish-start))
