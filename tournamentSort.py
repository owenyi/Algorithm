def tournamentSort(a, n):
    N = 1
    while N < n:
        N *= 2
    b = [0]*(N*2)
    for j in range(n):
        b[N + j] = a[j + 1]
    for i in range(n):
        for j in range(N*2 - 1, 2, -2):
            if b[j] > b[j - 1]:
                b[int(j/2)] = b[j]
            else:
                b[int(j/2)] = b[j - 1]
        a[n - i] = b[1]
        for k in range(N, N*2):
            if b[k] == b[1]:
                b[k] = 0
                break

def checkSort(a,n):
    isSorted=True
    for i in range(1,n):
        if (a[i] > a[i+1]):
            isSorted=False
        if (not isSorted):
            break
    if isSorted:
        print("정렬완료")
    else:
        print("정렬 오류 발생")

# def tournamentSort(a, n):
#     N = 1
#     while N < n:
#         N *= 2
#     b = [[0, 0]]*(N*2)
#     for j in range(0, n):
#         b[N + j] = [N + j, a[j + 1]]
#     for i in range(n):
#         for j in range(N * 2 - 1, 2, -2):
#             if b[j][1] > b[j - 1][1]:
#                 b[int(j / 2)] = b[j]
#             else:
#                 b[int(j / 2)] = b[j - 1]
#         a[n - i] = b[1][1]
#         b[b[1][0]] = [0, 0]
        # for k in range(N*2):
        #     print(b[k][1], end = ' ')
        # print()

import random, time

print('10000(in order)')
a = [i for i in range(1, 10001)]
a.insert(0, -1)
start = time.time()
tournamentSort(a, len(a) - 1)
end_time = time.time() - start
checkSort(a, len(a) - 1)
print('실행시간 :', end_time)

print('10000(random)')
a = [i for i in range(1, 10001)]
random.shuffle(a)
a.insert(0, -1)
start = time.time()
tournamentSort(a, len(a) - 1)
end_time = time.time() - start
checkSort(a, len(a) - 1)
print('실행시간 :', end_time)

print('10000(reverse)')
a = [i for i in range(10000, 0, -1)]
a.insert(0, -1)
start = time.time()
tournamentSort(a, len(a) - 1)
end_time = time.time() - start
checkSort(a, len(a) - 1)
print('실행시간 :', end_time)