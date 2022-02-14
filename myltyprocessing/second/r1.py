import multiprocessing


def worker(q):
    q.put('X' * 1000000)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    obj = queue.get()
    print(obj)
    p.join()
