#!/dev/bin/python

import time

def read_file(filename="names.txt"):
    return open(filename, "r").read().replace("\"", "").split(",")

def gen(name):
    for char in name:
        yield ord(char)-64

def names_scores():
    names_list = sorted(read_file())
    compteur = 1
    total = 0

    for name in names_list:
        total += (compteur * sum(gen(name)))
        compteur +=1
    return total

if __name__ == "__main__":
    tStart = time.time()
    print("Anwser : {}".format(names_scores()))
    print("Done in {}s".format(time.time() - tStart))
