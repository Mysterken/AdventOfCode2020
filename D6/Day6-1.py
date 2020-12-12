data = open('input', 'r').read().split('\n\n')

List = []
for group in data:
    new = group.replace('\n', '')
    List.append(new)

sum = 0
for group in List:
    alrdy_answered = []
    for answer in group:
        if not answer in alrdy_answered:
            alrdy_answered.append(answer)
    sum += len(alrdy_answered)
print(sum)
