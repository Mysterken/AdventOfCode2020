3-2.py
data = open('input', 'r').read().split('\n')

data.pop(0)

s1 = s2 = s3 = s4 = s5 = 0
c1 = c2 = c3 = c4 = c5 = 0
loop = 0

for line in data:
    
    loop += 1
    s1 += 1
    s2 += 3
    s3 += 5
    s4 += 7

    while s4 > len(line):
        line += line
    
    if line[s1] == "#":
        c1 += 1
    if line[s2] == "#":
        c2 += 1
    if line[s3] == "#":
        c3 += 1
    if line[s4] == "#":
        c4 += 1
    
    if loop % 2 == 0:
        s5 += 1
        if line[s5] == "#":
            c5 += 1
print(c1*c2*c3*c4*c5)
