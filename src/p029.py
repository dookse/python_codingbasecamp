a = input()
if a.isupper():
    print('YES')
else:
    print('NO')

b = input()
c = [d for d in b if d.isupper()]
print(''.join(c))
