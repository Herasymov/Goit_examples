import threading


def myfunc():
    global stop
    while not stop:
        pass


stop = False
thr1 = threading.Thread(target=myfunc)
thr1.start()
i = 0
while thr1.is_alive():
    print("HEYY", i)
    i += 1
    if i == 5:
        stop = True
    pass


print('Thread is finished')