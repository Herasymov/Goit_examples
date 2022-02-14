import multiprocessing


def worker():
    print('hello')


multiprocessing.freeze_support()
multiprocessing.set_start_method('spawn')
p = multiprocessing.Process(target=worker)
p.start()