import threading


def myfunc(a, b):
    print('Sum :', a + b)


thr1 = threading.Thread(target = myfunc, args=(1, 2)).start()
print('Main thread')
