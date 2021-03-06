from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num = 4
# 4 threads will need to pass this barrier to get released.
b = Barrier(num)
names = ["Harsh", "Lokesh", "George", "Iqbal"]


def player():
    name = names.pop()
    sleep(randrange(2, 5))
    print("% s reached the barrier at: % s" % (name, ctime()))
    b.wait()


threads = []
print("Race starts now")

for i in range(num - 1):
    threads.append(Thread(target=player))
    threads[-1].start()

for thread in threads:
    thread.join()
print("Race over!")