import os

def path_to_data(data_folder: str, filename: str) -> str:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    return os.path.join(data_file, filename)

def store_drawing(drawing_data: list, data: str):
    drawing_data.append(data)

def process_drawing(drawing_data: list, stacks_dynamic: dict):
    num_of_stacks = len(drawing_data[-1].split())
    for num in range(num_of_stacks):
        stacks_dynamic[str((num + 1))] = []
    
    drawing_data.reverse()
    for line in drawing_data:
        if line == drawing_data[0]:
            continue
        else:
            line = line + ' '
            line_lenght = len(line)
            stack = 1
            # consider using .split() instead of couting characters in string
            for crate in range(4, line_lenght + 1, 4):
                # check if the crate is empty
                if line[crate - 4 : crate][1:2] == ' ':
                    pass
                else:
                    stacks_dynamic[str(stack)].append(line[crate - 4 : crate][1:2])
                stack += 1

def top_crates_on_stacks(stacks: dict) -> str:
    result = ''
    for stack in stacks:
        result += stacks[stack][-1]
    return result

def main():
    filepath = path_to_data('data', 'input.txt')
    drawing = True
    drawing_data = []
    moves = []
    stacks = {}

    with open(filepath, 'r') as file:
        for line in file:
            line = line.rstrip()
            if not line:
                drawing = False
            if drawing:
                store_drawing(drawing_data, line)
            elif line.startswith('move') and not drawing:
                moves.append(line.split())

    process_drawing(drawing_data, stacks)
    print('Starting stacks:')
    print(stacks)

    ''' Process the moves. Consider making into function
    Each move is a list element eg. ['move', '1', 'from', '2', 'to', '1']
    index 1 is the amount of crates to move
    from stack 2 (index 3) to stack 1 (index 5)
    '''
    for move in moves:
        amount_of_crates = int(move[1])
        from_stack = move[3]
        to_stack = move[5]
        crate_mover_9001 = []

        # Grab crates from stack
        for _ in range(amount_of_crates):
            crate_mover_9001.append(stacks[from_stack].pop(-1))
        crate_mover_9001.reverse()
        stacks[to_stack] = stacks[to_stack] + crate_mover_9001
    
    print('Resulting stacks:')
    print(stacks)
    print(top_crates_on_stacks(stacks))

if __name__ == '__main__':
    main()

