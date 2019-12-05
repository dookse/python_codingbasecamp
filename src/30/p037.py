# line = input()
line = '원범 원범 혜원 혜원 혜원 혜원 유진 유진'
lines = list(map(str, line))
max_i = 0

for i in range(0, len(lines)):
    if lines.count(lines[max_i]) < lines.count(lines[i]):
        max_i = i

print('{}(이)가 총 {}표로 반장이 되었습니다.'.format(lines[max_i], line.count(lines[max_i])))
