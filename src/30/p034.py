# data = input()
data = '176 156 155 165 166 169'
data = list(map(int, data.strip().split()))

if data == sorted(data):
    print('YES')
else:
    print('NO')
