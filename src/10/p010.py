cnt = int(input()) * 2

for i in range(1, cnt, 2):
    blank = int((cnt - i) / 2)
    print(' ' * blank, end='')
    print('*' * i)

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + ("*" * (2 * i - 1)))
