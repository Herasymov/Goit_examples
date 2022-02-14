import multiprocessing

def worker(q):
    q.put('hello')

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()