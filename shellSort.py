def shellSort(a, n):
    h = 1
    while h < n:
        h = 3*h +1
    while(h >= 1):
        for i in range(1 + h, n + 1, h):
            v = a[i]
            j = i
            while j >= h + 1 and a[j - 1] > v:
                a[j] = a[j - h]
                j -= h
            a[j] = v
        h = int(h/3)

import openpyxl
workbook = openpyxl.load_workbook('sort.xlsx')
worksheet = workbook['Sheet1']
import random, time

a = [3, 4, 8, 6, 1, 2, 9, 7 ]
a.insert(0, -1)
shellSort(a, len(a)-1)
print(a)

print('N = 5000')
a = [random.randint(1, 5000) for i in range(5000)]
a.insert(0, -1)
start = time.time()
shellSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['E2'] = end

print('N = 10000')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
shellSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['E3'] = end

print('N = 15000')
a = [random.randint(1, 15000) for i in range(15000)]
a.insert(0, -1)
start = time.time()
shellSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['E4'] = end

print('순차')
a = [i for i in range(1, 10000)]
a.insert(0, -1)
start = time.time()
shellSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['E5'] = end

print('역순')
a = [i for i in range(10000, 0, -1)]
a.insert(0, -1)
start = time.time()
shellSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['E6'] = end

print('랜덤')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
shellSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)
worksheet['E7'] = end

workbook.save('sort.xlsx')