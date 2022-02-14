from threading import Lock, Thread

lock = Lock()
g = 0


def add_one():
    global g
    print("1 before lock")
    lock.acquire()
    print("1 in lock")
    g += 1
    lock.release()
    print("1 after lock")


def add_two():
    global g
    print("2 before lock")
    lock.acquire()
    print("2 in lock")
    g += 2
    lock.release()
    print("2 after lock")

threads = []
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for thread in threads:
    """
    Waits for threads to complete before moving on with the main
    script.
    """
    thread.join()

print(g)