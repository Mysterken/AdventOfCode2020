data = open('input', 'r').read().split('\n')

# Failed this one

instruc = []
for line in data:
    instruc.append([line[:3], int(line[4:].replace('+', ''))])

def reset():
    return instruc
instruction = reset()

index_already_done = []
accumulator = 0
changed_index = 0

def execute(command, value, index):

    global accumulator, changed_index, index_already_done, instruction

    if index in index_already_done:

        index_already_done = []
        
        for i in range(changed_index, len(instruction)):
            
            print(changed_index)
            instruction = reset()
            changed_index += 1
            accumulator = 0

            if instruction[i][0] == 'jmp':
                instruction[i][0] = 'nop'
            elif instruction[i][0] == 'nop':
                instruction[i][0] = 'jmp'

            if instruction[i][0] != 'acc':
                index, increment = 0, 0

    
    index_already_done.append(index)

    increment = 1

    if command == 'acc':
        accumulator += value
    elif command == 'jmp':
        increment = value

    try:
        execute(instruction[index+increment][0], instruction[index+increment][1], (index+increment))
    except IndexError:
        return

execute(instruction[0][0], instruction[0][1], 0)
print(accumulator)
