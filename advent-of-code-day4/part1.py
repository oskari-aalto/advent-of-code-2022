import os, csv

def path_to_data(data_folder: str, filename: str) -> str:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    return os.path.join(data_file, filename)

def main():
    filepath = path_to_data('data', 'input.csv')
    result = 0

    with open(filepath, 'r') as csvfile:
        reader_obj = csv.reader(csvfile)
        for row in reader_obj:
            pair1 = row[0].split('-')
            pair2 = row[1].split('-')
            pair1 = set(range(int(pair1[0]), int(pair1[1]) + 1))
            pair2 = set(range(int(pair2[0]), int(pair2[1]) + 1))
            
            overlap = pair1.intersection(pair2)
            if overlap == pair1 or overlap == pair2:
                result += 1
    print(result)                       

if __name__ == '__main__':
    main()

