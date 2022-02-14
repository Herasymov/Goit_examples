import threading
import time


def myfunc(a, b):
    time.sleep(0.2)
    print('Sum :', a + b)


thr1 = threading.Thread(target=myfunc, args=(1, 2), daemon=True)
thr1.start()
thr1.join(0.125)

if thr1.is_alive():
    print('Thread is alive')
else:
    print('Finish')
