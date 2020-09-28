def countingSort(a, n, m):
    count = [0] * (m + 1)
    for i in range(1, n + 1):
        count[a[i]] += 1
    for j in range(2, m + 1):
        count[j] = count[j - 1] + count[j]
    b = [0]*(n + 1)
    for i in range(n, 0, -1):
        b[count[a[i]]] = a[i]
        count[a[i]] -= 1
    for i in range(1, n + 1):
        a[i] = b[i]

# a = [0, 2, 1, 3, 5, 1, 2, 4, 4, 5, 5]
# n = 10
# m = 5
# countingSort(a, n, m)
# print('a')
# print(a)

import random
import time

print('N = 십만, M = 천')
N = 100000
M = 1000
a = [random.randint(1, M) for i in range(N)]
a.insert(0, 0)
start = time.time()
countingSort(a, N, M)
end = time.time() - start
print("실행시간 :", end)

print('N = 이십만, M = 천')
N = 200000
M = 1000
a = [random.randint(1, M) for i in range(N)]
a.insert(0, 0)
start = time.time()
countingSort(a, N, M)
end = time.time() - start
print("실행시간 :", end)

print('N = 삼십만, M = 천')
N = 300000
M = 1000
a = [random.randint(1, M) for i in range(N)]
a.insert(0, 0)
start = time.time()
countingSort(a, N, M)
end = time.time() - start
print("실행시간 :", end)