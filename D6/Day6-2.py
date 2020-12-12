data = open('input', 'r').read().split('\n\n')

List = []
for group in data:
    new = group.rsplit('\n')
    List.append(new)

sum = 0
for group in List:
    IA = []
    AL = ''
    for person in group:
        for answer in person:
            AL += answer
            if not answer in IA:
                IA.append(answer)
    for individual_answer in IA:
        if AL.count(individual_answer) == len(group):
            sum += 1
print(sum)
