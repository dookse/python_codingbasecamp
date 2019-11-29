n = '수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성'.split(',')
a = 'Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune'.split(',')
d = {n[i].strip(): a[i].strip() for i in range(0, len(n))}

req = input()
print(d[req])
