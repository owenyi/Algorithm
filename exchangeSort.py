def exchangeSort(a, n):
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if a[j] > a[i]:
                a[i], a[j] = a[j], a[i]

a = [-1,3,1,2,4,6,5]
exchangeSort(a, len(a) - 1)
print(a)

# import random, time
#
# print('N = 5000')
# a = [random.randint(1, 5000) for i in range(5000)]
# a.insert(0, -1)
# start = time.time()
# exchangeSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
#
# print('N = 10000')
# a = [random.randint(1, 10000) for i in range(10000)]
# a.insert(0, -1)
# start = time.time()
# exchangeSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
#
# print('N = 15000')
# a = [random.randint(1, 15000) for i in range(15000)]
# a.insert(0, -1)
# start = time.time()
# exchangeSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
#
# print('순차')
# a = [i for i in range(1, 10000)]
# a.insert(0, -1)
# start = time.time()
# exchangeSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
#
# print('역순')
# a = [i for i in range(10000, 0, -1)]
# a.insert(0, -1)
# start = time.time()
# exchangeSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)
#
# print('랜덤')
# a = [random.randint(1, 10000) for i in range(10000)]
# a.insert(0, -1)
# start = time.time()
# exchangeSort(a, len(a)-1)
# end = time.time() - start
# print("실행시간 :", end)