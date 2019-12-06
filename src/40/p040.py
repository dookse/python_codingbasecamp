limit = int(input())
count = int(input())
weights = []

for i in range(count):
    weights.append(int(input()))

result = 0
for w in weights:
    limit -= w
    if limit < 0:
        break
    result += 1

print(result)
