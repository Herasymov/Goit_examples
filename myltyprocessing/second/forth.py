import multiprocessing


def worker(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()
