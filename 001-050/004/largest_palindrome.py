#!/dev/bin/python

import time

def largest_pal():
    result = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            value = str(i*j)
            if value == value[::-1] :
                value = int(value)
                if value > result:
                    result = value
    return result

if __name__ == "__main__":
    start = time.time()
    print("Answer : {0}".format(largest_pal()))
    print("Done in {0}s".format(time.time() - start))

