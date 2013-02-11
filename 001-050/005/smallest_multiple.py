#!/dev/bin/python

import time

def smallest_multiple():
    result = 1
    for mod in range(1,21):
        if result % mod > 0:
            for j in range(1,21):
                if (result*j) % mod == 0:
                    result *= j
                    break
    return result

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {0}".format(smallest_multiple()))
    print("Done in {0}s".format(time.time() - tStart))

