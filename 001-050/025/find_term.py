#!/dev/bin/python

import time

#   Find the first term in Fibonacci sequence to contain 1000 digits
def find_term():
    a, b, count = 0, 1, 1

    while True:
        a, b = b, a+b
        count += 1

        if len(str(b)) == 1000:
            break
    return count

if __name__ == "__main__":
    start = time.time()
    print("Answer : {0}".format(find_term())) 
    print("Done in {0}s".format(time.time() - start))
