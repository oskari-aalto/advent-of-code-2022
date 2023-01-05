import os

def path_to_data(data_folder: str, filename: str) -> str:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    return os.path.join(data_file, filename)

def top_crates_on_stacks(stacks: dict) -> str:
    result = ''
    for stack in stacks:
        result += stacks[stack][-1]
    return result

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
            for crate in range(4, line_lenght + 1, 4):
                if line[crate - 4 : crate][1:2] == ' ':
                    pass
                else:
                    stacks_dynamic[str(stack)].append(line[crate - 4 : crate][1:2])
                stack += 1
            
    print(stacks_dynamic)

def main():
    filepath = path_to_data('data', 'input.txt')
    drawing = True
    drawing_data = []
    moves = []
    stacks = {}
    # stacks_hard_coded = {
    #         '1': ['P','F','M','Q','W','G','R','T'],
    #         '2': ['H','F','R'],
    #         '3': ['P','Z','R','V','G','H','S','D'],
    #         '4': ['Q','H','P','B','F','W','G'],
    #         '5': ['P','S','M','J','H'],
    #         '6': ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
    #         '7': ['P', 'T', 'H', 'N', 'M', 'L'],
    #         '8': ['F', 'D', 'Q', 'R'],
    #         '9': ['D', 'S', 'C', 'N', 'L', 'P', 'H']
    #         }

    with open(filepath, 'r') as file:
        for line in file:
            line = line.rstrip()
            if not line:
                drawing = False
            if drawing:
                store_drawing(drawing_data, line)
            elif line.startswith('move'):
                moves.append(line.split())

        process_drawing(drawing_data, stacks)

        for move in moves:
            crates = int(move[1])
            from_stack = move[3]
            to_stack = move[5]
            while crates > 0:
                stacks[to_stack].append(stacks[from_stack].pop())
                crates -= 1
    print(top_crates_on_stacks(stacks))
    

if __name__ == '__main__':
    main()

