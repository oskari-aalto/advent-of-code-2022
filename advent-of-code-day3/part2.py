import os
from string import ascii_letters

def path_to_data(data_folder: str, filename: str) -> str:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    return os.path.join(data_file, filename)

def item_priority(items: list) -> int:
    sum_of_priorities = 0
    for item in items:
        sum_of_priorities += ascii_letters.index(item) + 1
    return sum_of_priorities

def group_badge_item(items: list) -> str:
    badge_item = ''
    item_pool = ''
    for rucksack in items:
        item_pool += ''.join(rucksack)
    for char in item_pool:
        if item_pool.count(char) == 3:
            badge_item = char
    return badge_item

def main():
    filepath = path_to_data('data', 'input.txt')
    badge_items = []
    group_size = 3
    elf_group_rucksacks = []

    with open(filepath, 'r') as file:
        for r, line in enumerate(file):
            rucksack = set(line.strip())
            elf_group_rucksacks.append(rucksack)
            group_size -= 1
            if group_size == 0:
                badge_items.append(group_badge_item(elf_group_rucksacks))
                group_size = 3
                elf_group_rucksacks = []
    
    print(item_priority(badge_items))

if __name__ == '__main__':
    main()

