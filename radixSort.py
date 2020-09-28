def radixSort(a, n, m, Q):
    for k in range(1, m + 1):
        for i in range(1, n + 1):
            kd = digit(a[i], k)
            enqueue(Q[kd], a[i])
        p = 0
        for i in range(10):
            while Q[i] != []:
                p += 1
                a[p] = dequeue(Q[i])

def digit(data, k):
    l = 1
    for i in range(k - 1):
        l *= 10
    return int(data % (l * 10) / l)

def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if len(queue) == 0:
        print('큐가 공백임')
        return -1
    else:
        data = queue.pop(0)
        return data

# a = [-1, 832, 690, 152, 5, 950, 965, 369, 241, 577, 875]
# n = 10
# m = 3
# radixSort(a, n, m)
# print(a)

import random, time

Q = [[] for _ in range(10)]

print('100000(random)')
M = 5
N = 100000
a = [random.randint(1, 99999) for _ in range(100000)]
a.insert(0, -1)
start = time.time()
radixSort(a, N, M, Q)
print('실행시간 :', time.time() - start)

print('200000(random)')
M = 5
N = 200000
a = [random.randint(1, 99999) for _ in range(200000)]
a.insert(0, -1)
start = time.time()
radixSort(a, N, M, Q)
print('실행시간 :', time.time() - start)