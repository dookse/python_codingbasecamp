line = ''
for i in range(101):
    line += str(i)

result = 0
for i in line:
    result += int(i)

print(result)
