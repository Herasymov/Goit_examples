import multiprocessing


def worker(q):
    q.put('hello')


if __name__ == '__main__':
    ctx = multiprocessing.get_context('fork')
    q = ctx.Queue()
    p = ctx.Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()