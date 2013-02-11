#!/dev/bin/python

import time

def mult():
    for a in range(1, 1001):
        for b in range(a, 1001):
            c = 1000-b-a
            if (((a**2) + (b**2)) == (c**2)):
                return a*b*c
    

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {0}".format(mult()))
    print("Done in {0}s".format(time.time() - tStart))

