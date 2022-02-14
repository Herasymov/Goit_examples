import multiprocessing


def worker(lock, i):
    lock.acquire()
    try:
        print('hello world', i)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = multiprocessing.Lock()

    for num in range(10):
        multiprocessing.Process(target=worker, args=(lock, num)).start()
