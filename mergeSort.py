def mergeSort(a, l, r):
    if r > l:
        m = int((r+l)/2)
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)

def merge(a, l, m, r):
    i, j, k = l, m + 1, l
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            b[k] = a[j]
            k += 1
            j += 1
    if i > m:
        for p in range(j, r + 1):
            b[k] = a[p]
            k += 1
    else:
        for p in range(i, m + 1):
            b[k] = a[p]
            k += 1
    for p in range(l, r + 1):
        a[p] = b[p]

import random, time

print('100000(random)')
a = [random.randint(1, 100000) for _ in range(100000)]
a.insert(0, -1)
b = a.copy()
start = time.time()
mergeSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)

print('200000(random)')
a = [random.randint(1, 200000) for _ in range(200000)]
a.insert(0, -1)
b = a.copy()
start = time.time()
mergeSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)

print('1000000(random)')
a = [random.randint(1, 1000000) for _ in range(1000000)]
a.insert(0, -1)
b = a.copy()
start = time.time()
mergeSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)

#민감도
print('100000(in order)')
a = [i for i in range(100000)]
a.insert(0, -1)
b = a.copy()
start = time.time()
mergeSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)

print('100000(random)')
a = [random.randint(1, 100000) for _ in range(100000)]
a.insert(0, -1)
b = a.copy()
start = time.time()
mergeSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)

print('100000(reverse)')
a = [i for i in range(100000, 0, -1)]
a.insert(0, -1)
b = a.copy()
start = time.time()
mergeSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)