#!/dev/bin/usr

import time

#Too long...
#Maybe using cache system (with dictionnay ?)

def collatz_sequence(n):
    length = 1

    while n != 1:
        length += 1
        if n & 1:
            n = (3 * n) + 1
        else:
            n = n//2
    return length

def find_greater(n_max=999999):
    max_len_pos = (0, 0)
    for i in range(n_max, 499999, -2):
        length = collatz_sequence(i)
        if length > max_len_pos[0]:
            max_len_pos = (length, i)
    return max_len_pos[1]
    

if __name__ == "__main__":
    tStart = time.time()
    print("Answer : {}".format(find_greater()))
    print("Done in {}s".format(time.time() - tStart))
