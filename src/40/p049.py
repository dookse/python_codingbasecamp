line = '10 9 8 7 6 5 4 3 2 1'
num_list = list(map(int, line.split()))

print(max(num_list))
print(sorted(num_list)[-1])
