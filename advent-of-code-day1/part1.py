import os

def main():
    filename = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    filepath = os.path.join(data_file, filename)

    most_calories: int = 0
    elf_calories: int = 0

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                if elf_calories > most_calories:
                    most_calories = elf_calories
                elf_calories = 0
                continue
            else:
                elf_calories += int(line)
    
    print(most_calories)

if __name__ == '__main__':
    main()