data = open('input', 'r').read().split('\n')

def get(num):
    List = []
    for a in range(0,num):
        List.append(a)
    return List

max = 0
for PASS in data:
    R, C = get(128), get(8)
    for i in range(len(PASS)):
        removeR, removeC = len(R)/2, len(C)/2
        if PASS[i] == 'F':
            while len(R) != removeR:
                R.pop(-1)
        elif PASS[i] == 'B':
            while len(R) != removeR:
                R.pop(0)
        elif PASS[i] == 'L':
            while len(C) != removeC:
                C.pop(-1)
        elif PASS[i] == 'R':
            while len(C) != removeC:
                C.pop(0)
    if (int(R[0])*8+int(C[0])) > max:
        max = int(R[0])*8+int(C[0])  
print(max)
