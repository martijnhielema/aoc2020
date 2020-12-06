def seat_id(input: str) -> int:
    row = input[0:7].replace('F', '0').replace('B', '1')
    column = input[7:].replace('L', '0').replace('R', '1')

    row_number = int(row, 2)
    column_number = int(column, 2)

    return 8 * row_number + column_number


if __name__ == '__main__':
    with open('../input/day5.txt', 'r') as f:
        boarding_passes = [bpass.strip() for bpass in f.readlines()]

    seat_ids = [*map(seat_id, boarding_passes)]
    print(f'Highest seat ID: {max(seat_ids)}')

    sorted_seats = sorted(list(seat_ids))
    for i in range(1, len(sorted_seats) + 1):
        if sorted_seats[i] - sorted_seats[i-1] == 2:
            print(f'Your seat ID: {int((sorted_seats[i] + sorted_seats[i-1]) / 2)}')
            break
