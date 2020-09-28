def cocktailSort(a, n):
    i = n
    j = 1
    while i > j:
        k = 1
        while k <= i - 1:
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]
                print(a)
            k += 1
        i -= 1
        while k >= j + 1:
            if a[k] < a[k - 1]:
                a[k], a[k - 1] = a[k - 1], a[k]
                print(a)
            k -= 1
        j += 1

a =[-1, 6, 5, 4, 3, 2, 1]
cocktailSort(a, len(a) - 1)
