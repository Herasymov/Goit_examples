import multiprocessing


def worker(l):
    l.acquire()
    try:
        print('hello world')
    finally:
        l.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for i in range(10):
        multiprocessing.Process(target=worker, args=(lock,)).start()