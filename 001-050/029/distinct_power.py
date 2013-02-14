#!/dev/bin/python

import time

def gen(a_max=100, b_max=100):
    for a in range(2, a_max+1):
        for b in range(2, b_max+1):
            yield a**b

def distinct_power():
    return len(set(gen()))

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {}".format(distinct_power()))
    print("Done in {}s".format(time.time() - tStart))
