import random
import numpy as np

A = [[ 2, -3, 3, 5],
[-2, 6, 5, -2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7],
[ 1, 2, 3]]

#Row
#print(len(A))
#Column
#print(len(A[0]))
'''
for i in range(len(A)):
    print(i,"A")
    for j in range(len(B[0])):
        print(j, "B")
        for k in range(len(B)):
            print(k, "C")

C = [[0 for i in range(len(B)-1)] for j in range(len(A))]
for row in C:
    print(row)

if len(A) == len(B[0]):
    print("True")
else:
    print("False")


def isPrime(p):
    prime = False
    while prime == False:
        for i in np.arange(2, p):
            if p%i == 0:
                prime = True
                return True
            prime = False
            return False


print(isPrime(7))

def nBitPrime(n):
    noPrime = True
    while noPrime:
        randFloat = random.random()
        randNum = round(randFloat*(2**n))
        primeBool = isPrime(randNum)
        if primeBool is True and randNum >= 2:   # I feel like the randNum >= 2 is redundant
            noPrime = False
            return randNum

print(nBitPrime(2))
'''
'''
def nBitPrime(n):
    value = 0
    while not value >= 2 and not isPrime(value) == True:
        value = round((random.random() * 2**n), 2)
        return value
'''

'''
def isPrime(p):
    for i in range(2, p):
        if p%i == 0:
            return False
    return True
'''

'''ogp = nBitPrime(13)
ogq = nBitPrime(13)
testpq = ogp * ogq
print("OGP:", ogp, "OGQ:", ogq, "pq:", testpq)'''

a = []
for i in range(9,26,2):
    print(i)