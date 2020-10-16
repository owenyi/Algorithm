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

def selectionSort(a, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i, n + 1):
            if (a[j] < a[minIndex]): minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]

a = [-1, 4, 8 ,5, 6, 1, 3, 7, 2]
selectionSort(a, len(a) - 1)
checkSort(a, len(a) - 1)