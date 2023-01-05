import os

def path_to_data(data_folder: str, filename: str) -> str:
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    return os.path.join(data_file, filename)

def round_points(round: list) -> int:
    # ['C', 'Z']
    # rock(A) = 1, paper(B) = 2, scissors(C) = 3
    shape_points: dict = {'A': 1, 'B': 2, 'C': 3}
    # X = loss, Z = draw, Y = win
    result_points: dict = {'Loss': 0, 'Draw': 3, 'Win': 6}
    round_points = 0

    if round[0] =='A':
        if round[1] == 'X':
            round_points += result_points['Draw']
            round_points += shape_points['A']
        elif round[1] == 'Y':
            round_points += result_points['Win']
            round_points += shape_points['B']
        elif round[1] == 'Z':
            round_points += result_points['Loss']
            round_points += shape_points['C']
    elif round[0] =='B':
        if round[1] == 'X':
            round_points += result_points['Loss']
            round_points += shape_points['A']
        elif round[1] == 'Y':
            round_points += result_points['Draw']
            round_points += shape_points['B']
        elif round[1] == 'Z':
            round_points += result_points['Win']
            round_points += shape_points['C']
    if round[0] =='C':
        if round[1] == 'X':
            round_points += result_points['Win']
            round_points += shape_points['A']
        elif round[1] == 'Y':
            round_points += result_points['Loss']
            round_points += shape_points['B']
        elif round[1] == 'Z':
            round_points += result_points['Draw']
            round_points += shape_points['C']
    return round_points

def main():
    filepath = path_to_data('data', 'input.txt')
    total_score: int = 0

    with open(filepath, 'r') as file:
        for r, line in enumerate(file):
            round = line.strip().split()
            total_score += round_points(round)
            print(r, total_score)
  
    print(total_score)

if __name__ == '__main__':
    main()

