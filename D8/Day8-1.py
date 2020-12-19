data = open('input', 'r').read().split('\n')

instruction = []
for line in data:
    instruction.append([line[:3], int(line[4:].replace('+', ''))])

index_already_done = []
accumulator = 0

def execute(command, value, index):

    global accumulator, index_already_done, instruction
    
    if index in index_already_done:
        return accumulator
    index_already_done.append(index)

    increment = 1

    if command == 'acc':
        accumulator += value
    elif command == 'jmp':
        increment = value
    execute(instruction[index+increment][0], instruction[index+increment][1], (index+increment))

execute(instruction[0][0], instruction[0][1], 0)
print(accumulator)
