def quickSort(a, l, r):
    if r > l:
        i = partition(a, l, r)
        quickSort(a, l, i - 1)
        quickSort(a, i + 1, r)

def partition(a, l, r):
    v = a[r]
    i = l - 1
    j = r
    while True:
        i = i + 1
        while a[i] < v: i = i + 1
        j = j - 1
        while a[j] > v: j = j - 1
        if i >= j: break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i;

import random, time

print('100000(random)')
a = [random.randint(1, 100000) for _ in range(100000)]
a.insert(0, -1)
start = time.time()
quickSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)

print('200000(random)')
a = [random.randint(1, 200000) for _ in range(200000)]
a.insert(0, -1)
start = time.time()
quickSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)

print('1000000(random)')
a = [random.randint(1, 1000000) for _ in range(1000000)]
a.insert(0, -1)
start = time.time()
quickSort(a, 1, len(a)-1)
print('실행시간 :', time.time() - start)
