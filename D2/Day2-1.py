data = open('input', 'r').read().split('\n')

def Requirement(string):
    for x in range(4, 6):
        try:
            Min = int(string[0:x-3])
            Max = int(string[(x-2):x])
            if x == 4:
                Letter = string[x:x+1]
                Password = string[(x+1)+2:]
            else:
                Letter = string[x:x+2]
                Password = string[(x+2)+2:]
            int(Letter)
        except ValueError:
            if Letter == " ":
                Letter = string[x+1:x+2]
                Password = string[(x+2)+2:]
                break
    RQList = [Min, Max, Letter.strip(), Password]
    return RQList

ValidPassword=0
for i in range(len(data)):
    Counter = 0
    RQ = Requirement(data[i]) 
    PW = RQ[3]
    while PW.find(RQ[2]) != -1:
        Counter += 1
        PW = PW[:PW.find(RQ[2])] + PW[PW.find(RQ[2])+1:]
    if RQ[0] <= Counter <= RQ[1]:
        ValidPassword += 1
print(ValidPassword)
