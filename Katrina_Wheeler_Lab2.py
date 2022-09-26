import random
from time import time

def merge(A,B):
    out = []
    i,j = 0,0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)

def insertionSort(L):
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A

def bubbleSort(L):
    n = len(L)
    swapped = False
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                swapped = True
                L[j], L[j+1] = L[j+1], L[j]
        if not swapped:
            return

print("N", "Bubble", "Insertion", "Merge")

for n in range(100, 5100, 100):
    A = [i for i in range(n)]

    #bubble sort
    random.shuffle(A)
    t1 = time()
    B = bubbleSort(A)
    t2 = time()
    btime = round(((t2 - t1) * 1000), 2)

    #insertion sort
    random.shuffle(A)
    u1 = time()
    I = insertionSort(A)
    u2 = time()
    itime = round(((u2 - u1) * 1000), 2)

    #merge sort
    random.shuffle(A)
    v1 = time()
    M = mergeSort(A)
    v2 = time()
    mtime = round(((v2 - v1) * 1000), 2)

    print(n, " : ", btime, " ", itime, " ", mtime)