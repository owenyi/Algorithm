def naturalMergeSort(a, l, r):
    run = [l - 1]
    i = 1
    while i < r:
        if a[i] > a[i + 1]:
            run.append(i)
        i += 1
    run.append(r)

    Len = len(run) - 1
    cnt = 1
    while (cnt < Len/2):
        cnt *= 2
    n = 1
    while n <= cnt:
        m = n*2
        while m < Len:
            merge(a, run[m - n*2] + 1, run[m - n], run[m])
            print(a)
            m += n*2
        if m - n < Len:
            merge(a, run[m - n*2] + 1, run[m - n], r)
            print(a)
        else:
            merge(a, run[m - n*2] + 1, r, r)
            print(a)
        n *= 2

def merge(a, l, m, r):
    b = a.copy()
    i, j, k = l, m + 1, l
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            b[k] = a[j]
            k += 1
            j += 1
    if i > m:
        for p in range(j, r + 1):
            b[k] = a[p]
            k += 1
    else:
        for p in range(i, m + 1):
            b[k] = a[p]
            k += 1
    for p in range(l, r + 1):
        a[p] = b[p]

a = [-1,6,7,8,3,4,12,11,1,5,9,10,2]
naturalMergeSort(a, 1, len(a) - 1)

