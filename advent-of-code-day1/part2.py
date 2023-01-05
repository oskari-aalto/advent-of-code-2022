import os

def path_to_folder_in_maindir(data_folder: str, filename: str) -> str:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    return os.path.join(data_file, filename)

def main():
    
    filepath = path_to_folder_in_maindir('data', 'input.txt')
    elves_calories: list = []
    single_elf_calories: int = 0


    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                elves_calories.append(single_elf_calories)
                single_elf_calories = 0
                continue
            else:
                single_elf_calories += int(line)
    
    elves_calories.sort()
    print(sum(elves_calories[-3:]))

if __name__ == '__main__':
    main()