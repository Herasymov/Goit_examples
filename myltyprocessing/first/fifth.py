import multiprocessing
import time

def sleepy_man(sec):
    print('Starting to sleep')
    time.sleep(sec)
    print('Done sleeping')

tic = time.time()

process_list = []
for i in range(10):
    p =  multiprocessing.Process(target= sleepy_man, args=[0.5])
    p.start()
    process_list.append(p)

for process in process_list:
    process.join()

toc = time.time()

print('Done in {:.4f} seconds'.format(toc-tic))