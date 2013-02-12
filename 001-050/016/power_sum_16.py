#!/dev/bin/python

import time

def _sum(number=2**1000):
    return sum(map(int, list(str(number))))

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {}".format(_sum()))
    print("Done in {}s".format(time.time() - tStart))
