import time


def please_sleep(n):
    print("Sleeping for {} seconds".format(n))
    time.sleep(n)
    print("Done Sleeping")


start = time.perf_counter()
for i in range(1,5):
   please_sleep(i)

finish = time.perf_counter()
print("Finished in {} seconds".format(finish-start))
