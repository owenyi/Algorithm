NUM = 27
def index(c):
    if ord(c) == 32: return 0
    else: return ord(c) - 64

def initSkip(p):
    M = len(p)
    skip = [M]*NUM
    for i in range(M):
        skip[index(p[i])] = M - i - 1
    return(skip)

def BM(p, t, k):
    M = len(p)
    N = len(t)
    skip = initSkip(p)
    i = k + M - 1
    j = M - 1
    if i >= N: return N
    while j >= 0:
        while t[i] != p[j]:
            s = skip[index(t[i])]
            if M - j > s: i += M - j
            else: i += s
            if i >= N: return N
            j = M - 1
        i -= 1
        j -= 1
    return i + 1

text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
pattern = 'ATION'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = BM(pattern, text, K)
    K = pos + M
    if K <= N: print('패턴이 나타난 위치 :', pos)
    else: break
print('스트링 탐색 종료')