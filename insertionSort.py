def insertionSort(a, n):
    i = 1
    while i <= n:
        v = a[i]
        j = i
        while a[j-1] > v:
            a[j] = a[j - 1]
            j -= 1
        a[j] = v
        i += 1

import openpyxl
workbook = openpyxl.load_workbook('sort.xlsx')
worksheet = workbook['Sheet1']
import random, time

a = [3, 4, 8, 6, 1, 2, 9, 7 ]
a.insert(0, -1)
insertionSort(a, len(a)-1)
print(a)

print('N = 5000')
a = [random.randint(1, 5000) for i in range(5000)]
a.insert(0, -1)
start = time.time()
insertionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['D2'] = end

print('N = 10000')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
insertionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['D3'] = end

print('N = 15000')
a = [random.randint(1, 15000) for i in range(15000)]
a.insert(0, -1)
start = time.time()
insertionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['D4'] = end

print('순차')
a = [i for i in range(1, 10000)]
a.insert(0, -1)
start = time.time()
insertionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['D5'] = end

print('역순')
a = [i for i in range(10000, 0, -1)]
a.insert(0, -1)
start = time.time()
insertionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['D6'] = end

print('랜덤')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
insertionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['D7'] = end

workbook.save('sort.xlsx')