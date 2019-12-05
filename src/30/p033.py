data = input()
print(data.strip()[::-1])

datas = data.strip().split()
datas.sort(reverse=True)
for d in datas:
    print(d, end='')

print()
datas = data.strip().split()
for i in range(len(datas) - 1, -1, -1):
    print(datas[i], end=' ')
