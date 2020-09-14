def bubbleSort(a, n):
    for i in range(n, 1, -1):
        for j in range(1, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

import openpyxl
workbook = openpyxl.load_workbook('sort.xlsx')
worksheet = workbook['Sheet1']
import random, time

a = [3, 4, 8, 6, 1, 2, 9, 7 ]
a.insert(0, -1)
bubbleSort(a, len(a)-1)
print(a)

print('N = 5000')
a = [random.randint(1, 5000) for i in range(5000)]
a.insert(0, -1)
start = time.time()
bubbleSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['C2'] = end

print('N = 10000')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
bubbleSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['C3'] = end

print('N = 15000')
a = [random.randint(1, 15000) for i in range(15000)]
a.insert(0, -1)
start = time.time()
bubbleSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['C4'] = end

print('순차')
a = [i for i in range(1, 10000)]
a.insert(0, -1)
start = time.time()
bubbleSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['C5'] = end

print('역순')
a = [i for i in range(10000, 0, -1)]
a.insert(0, -1)
start = time.time()
bubbleSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['C6'] = end

print('랜덤')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
bubbleSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['C7'] = end

workbook.save('sort.xlsx')
