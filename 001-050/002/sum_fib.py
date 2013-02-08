#!/dev/bin/python

#   Find the sum of the even-valued terms of Fibonacci sequence for each terms below 4 milions
def _sum():
    a, b, res = 0, 1, 0

    while True:
        a, b = b, a+b
        
        if b >= 4000000:
            break
        if b % 2 == 0:
            res += b
    return res

if __name__ == "__main__":
    print("Anwser : {0}".format(_sum()))
