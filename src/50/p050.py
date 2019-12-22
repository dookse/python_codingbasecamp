def bubble(n, data):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    for i in range(n):
        print(data[i], end=' ')


request = '4 2 3 5 8'.split()
data = list(map(int, request))
n = len(request)

bubble(n, data)
