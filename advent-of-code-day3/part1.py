import os
from string import ascii_letters


def path_to_data(data_folder: str, filename: str) -> str:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    return os.path.join(data_file, filename)

def rucksack_size(items: str) -> tuple:
    total_items = len(items)
    half_of_items = total_items // 2
    return (0, half_of_items, total_items)

def item_priority(duplicate_items: list) -> int:
    sum_of_priorities = 0
    for item in duplicate_items:
        sum_of_priorities += ascii_letters.index(item) + 1
    return sum_of_priorities

def main():
    filepath = path_to_data('data', 'test.txt')
    duplicate_items = []

    with open(filepath, 'r') as file:
        for r, line in enumerate(file):
            rucksack = line.strip()
            compartments = rucksack_size(rucksack)
            first_compartment_items = rucksack[:compartments[1]]
            second_compartment_items = rucksack[compartments[1]:]

            for char in first_compartment_items:
                if char in second_compartment_items:
                    duplicate_items.append(char)
                    break
    
    print(item_priority(duplicate_items))

if __name__ == '__main__':
    main()

