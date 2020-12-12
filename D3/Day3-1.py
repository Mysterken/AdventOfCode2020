data = open('input', 'r').read().split('\n')

data.pop(0)

x = 0
count = 0
for line in data:
    x += 3
    while x > len(line):
        line += line
    if line[x] == "#":
            count += 1
print(count)
