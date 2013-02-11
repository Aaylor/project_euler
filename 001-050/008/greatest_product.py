#!/dev/bin/python

import time

def find_greatest_product(liste):
    first_compteur, max_compteur = 0, 4
    result = 0
    while max_compteur < len(liste):
        zero = False
        if "0" in liste[first_compteur:max_compteur+1]:
            first_compteur += 4
            max_compteur += 4
        else:
            tmp = 1
            for i in liste[first_compteur:max_compteur+1]:
                tmp *= int(i)
            if tmp > result:
                result = tmp
            first_compteur += 1
            max_compteur += 1
    return result

if __name__ == "__main__":
    liste = list(str(73167176531330624919225119674426574742355349194934))
    liste.extend(list(str(96983520312774506326239578318016984801869478851843)))
    liste.extend(list(str(85861560789112949495459501737958331952853208805511)))
    liste.extend(list(str(12540698747158523863050715693290963295227443043557)))
    liste.extend(list(str(66896648950445244523161731856403098711121722383113)))
    liste.extend(list(str(62229893423380308135336276614282806444486645238749)))
    liste.extend(list(str(30358907296290491560440772390713810515859307960866)))
    liste.extend(list(str(70172427121883998797908792274921901699720888093776)))
    liste.extend(list(str(65727333001053367881220235421809751254540594752243)))
    liste.extend(list(str(52584907711670556013604839586446706324415722155397)))
    liste.extend(list(str(53697817977846174064955149290862569321978468622482)))
    liste.extend(list(str(83972241375657056057490261407972968652414535100474)))
    liste.extend(list(str(82166370484403199890008895243450658541227588666881)))
    liste.extend(list(str(16427171479924442928230863465674813919123162824586)))
    liste.extend(list(str(17866458359124566529476545682848912883142607690042)))
    liste.extend(list(str(242190226710556263211111093705442175069416589604080)))
    liste.extend(list(str(7198403850962455444362981230987879927244284909188)))
    liste.extend(list(str(845801561660979191338754992005240636899125607176060)))
    liste.extend(list(str(5886116467109405077541002256983155200055935729725)))
    liste.extend(list(str(71636269561882670428252483600823257530420752963450)))

    tStart = time.time()
    print("Answer : {0}".format(find_greatest_product(liste)))
    print("Done in {0}s".format(time.time() - tStart))
