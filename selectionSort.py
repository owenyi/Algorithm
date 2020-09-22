def selectionSort(a, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i, n + 1):
            if (a[j] < a[minIndex]): minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]

import random, time

print('N = 5000')
a = [random.randint(1, 5000) for i in range(5000)]
a.insert(0, -1)
start = time.time()
selectionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)

print('N = 10000')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
selectionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)

print('N = 15000')
a = [random.randint(1, 15000) for i in range(15000)]
a.insert(0, -1)
start = time.time()
selectionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)

print('순차')
a = [i for i in range(1, 10000)]
a.insert(0, -1)
start = time.time()
selectionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)

print('역순')
a = [i for i in range(10000, 0, -1)]
a.insert(0, -1)
start = time.time()
selectionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)

print('랜덤')
a = [random.randint(1, 10000) for i in range(10000)]
a.insert(0, -1)
start = time.time()
selectionSort(a, len(a)-1)
end = time.time() - start
print("실행시간 :", end)

# import openpyxl
# workbook = openpyxl.load_workbook('sort.xlsx')
# worksheet = workbook['Sheet1']
# import random, time
#
# a = [3, 4, 8, 6, 1, 2, 9, 7 ]
# a.insert(0, -1)
# selectionSort(a, len(a)-1)
# print(a)
#
# print('N = 5000')
# a = [random.randint(1, 5000) for i in range(5000)]
# a.insert(0, -1)
# start = time.time()
# selectionSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
# worksheet['B2'] = end
#
# print('N = 10000')
# a = [random.randint(1, 10000) for i in range(10000)]
# a.insert(0, -1)
# start = time.time()
# selectionSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
# worksheet['B3'] = end
#
# print('N = 15000')
# a = [random.randint(1, 15000) for i in range(15000)]
# a.insert(0, -1)
# start = time.time()
# selectionSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
# worksheet['B4'] = end
#
# print('순차')
# a = [i for i in range(1, 10000)]
# a.insert(0, -1)
# start = time.time()
# selectionSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
# worksheet['B5'] = end
#
# print('역순')
# a = [i for i in range(10000, 0, -1)]
# a.insert(0, -1)
# start = time.time()
# selectionSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
# worksheet['B6'] = end
#
# print('랜덤')
# a = [random.randint(1, 10000) for i in range(10000)]
# a.insert(0, -1)
# start = time.time()
# selectionSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
# worksheet['B7'] = end
#
# workbook.save('sort.xlsx')