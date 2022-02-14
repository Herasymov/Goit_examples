import time
import multiprocessing

def is_perfect(n):
    sum_factors = 0
    for i in range(1, n):
        if(n % i == 0):
            sum_factors = sum_factors + i
    if (sum_factors == n):
        print('{} is a Perfect number'.format(n))

tic = time.time()

processes = []
for i in range(1, 10000):
    p = multiprocessing.Process(target=is_perfect, args=(i,))
    processes.append(p)
    p.start()

for process in processes:
    process.join()

toc = time.time()
print('Done in {:.4f} seconds'.format(toc-tic))
