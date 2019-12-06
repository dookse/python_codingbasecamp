line = '97 86 75 66 55 97 85 97 97 95 86'
# line = input()
lines = list(map(int, line.split()))
t = {i: lines.count(i) for i in lines}

result = 0
for i in range(3):
    max_key = max(t)
    result += t.pop(max_key)

print(result)
