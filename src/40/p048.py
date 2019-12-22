line = input()
result = []

for c in line:
    if c.isupper():
        result.append(c.lower())
    else:
        result.append(c.upper())

print(''.join(result))
