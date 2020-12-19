data = open('input', 'r').read().split('\n')

# Failed this one, work on the given exemple but not on input

bags = []
contain = []

# Append bag attribute and what it contain
for line in data:
    
    line = line.rsplit(' ')
    bags.append([line[0]+ ' '+ line[1]])
    inside_bag = []
    
    for i in range(5, len(line), 4):
        inside_bag.append([line[i]+' ' + line[i+1]])
    contain.append(inside_bag)

answer = 0
def search_all_inside(bag):
    global answer
    index = bags.index(bag)
    for i in range(len(contain[index])):

        if contain[index][i] == ['shiny gold']:
            print(bag)
            answer += 1
            return True
        elif contain[index][i] == ['other bags.']:
            return True
        else:
            if search_all_inside(bags[bags.index(contain[index][i])]):
                return

for bag in bags:
    print(f'bag is: {bag}')
    search_all_inside(bag)
print(answer)
