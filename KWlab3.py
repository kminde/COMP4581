import random
from math import sqrt
from time import time
import pandas as pd

# Takes in a number, returns false if it is not prime, true if it is prime
def isPrime(p):
    for i in range(2, int(sqrt(p))+1):
        if p%i == 0:
            return False
    return True

# Takes a random number, checks if it is prime/returns it, restarts if it is not
def nBitPrime(n):
    notprime = True
    while notprime:
        randVal = random.random()
        randNum = round(randVal*(2**n))
        checkPrime = isPrime(randNum)
        if checkPrime is True and randNum >= 2:
            notprime = False
            return randNum

# Determines factors of a given number
def factor(pq):
    p = 0
    q = 0
    for i in range(2, pq):
        if pq%i == 0:
            p = i
            q = pq/p
    return p,q

df1 = []
df2 = []

# Creates 2 random n-bit prime numbers, multiples them, then feeds
# that number into the factor function
for i in range (9, 22, 2):
    df1.append(i)
    t1 = time()
    p = nBitPrime(i)
    q = nBitPrime(i)
    pq = p*q
    testp, testq = factor(pq)
    t2 = time()
    totTime = round(((t2 - t1) * 1000), 2)
    df2.append(totTime)

col1 = "N"
col2 = "Time"
data = pd.DataFrame({col1:df1,col2:df2})
data.to_excel('prime_expo.xlsx')
