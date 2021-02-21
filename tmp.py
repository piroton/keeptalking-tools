with open('display.txt') as f:
    t = [i.strip() for i in f.readlines()]
print(t)
d = {}
for i in t:
    j = i.split(': ')
    k = j[0].strip('"')
    v = j[1]
    d[k] = v
print(d)
