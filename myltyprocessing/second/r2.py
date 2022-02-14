import multiprocessing

def worker():
    lock.acquire()
    try:
        print('hello world')
    finally:
        lock.release()


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    for i in range(10):
        multiprocessing.Process(target=worker).start()