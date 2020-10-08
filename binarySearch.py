class node:
    def __init__(self, key = None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def binarySearch(self, search_key):
        left = 0
        right = len(Dict.a) - 1
        while right >= left:
            mid = int((left + right)/2)
            if Dict.a[mid].key == search_key:
                return mid
            if Dict.a[mid].key > search_key:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def insert(self, v):
        Dict.a.append(node(v))

##quickSort
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
    return i
##qucikSort

import random, time
N = 10000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(key)
random.shuffle(s_key)
start_time = time.time()
quickSort(key, 0, N - 1)
d = Dict()
for i in range(N):
    d.insert(key[i])
for i in range(N):
    result = d.binarySearch(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색 오류')
end_time = time.time() - start_time
print('이진 탐색의 살행시간 (N = %d) : %0.3f'%(N, end_time))
print('탐색 완료')

N = 20000
key = list(range(1, N + 1))
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(key)
random.shuffle(s_key)
start_time = time.time()
quickSort(key, 0, N - 1)
d = Dict()
for i in range(N):
    d.insert(key[i])
for i in range(N):
    result = d.binarySearch(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색 오류')
end_time = time.time() - start_time
print('이진 탐색의 살행시간 (N = %d) : %0.3f'%(N, end_time))
print('탐색 완료')

N = 30000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(key)
random.shuffle(s_key)
start_time = time.time()
quickSort(key, 0, N - 1)
d = Dict()
for i in range(N):
    d.insert(key[i])
for i in range(N):
    result = d.binarySearch(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색 오류')
end_time = time.time() - start_time
print('이진 탐색의 살행시간 (N = %d) : %0.3f'%(N, end_time))
print('탐색 완료')