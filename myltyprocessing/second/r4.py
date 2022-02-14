import multiprocessing

def worker():
    print('hello')

p = multiprocessing.Process(target=worker)
p.start()