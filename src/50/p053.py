def check(line):
    size = len(line) // 2
    result = '(' * size + ')' * size
    return result


n = input()
if n == check(n):
    print('YES')
else:
    print('NO')
