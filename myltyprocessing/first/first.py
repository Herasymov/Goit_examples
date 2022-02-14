import time


def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')


tic = time.time()
sleepy_man()
sleepy_man()
toc = time.time()

print('Done in {:.4f} seconds'.format(toc-tic))
