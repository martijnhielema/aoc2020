with open('../input/day9.txt', 'r') as f:
    numbers = [int(n.strip('\n')) for n in f.readlines()]


def find_number(numlist:list, preamble: int) -> int:
    preamble_list = numlist[0: preamble]
    for i in range(preamble, len(numlist) + 1):
        found_sum = False
        for j in range(0, preamble):
            for k in range(j, preamble):
                if preamble_list[j] + preamble_list[k] == numlist[i]:
                    found_sum = True
                    break
            if found_sum:
                break

        if not found_sum:
            return numlist[i]
            break

        preamble_list.pop(0)
        preamble_list.append(numlist[i])


def find_range(number:int, lst: list):
    startpos = 0

    while True:
        sum = 0
        for i in range(startpos, len(lst)):
            sum += lst[i]
            if sum == number and i != startpos:
                print(startpos, i)
                print(numbers[startpos:i+1])
                minn = min(numbers[startpos:i+1])
                maxn = max(numbers[startpos:i+1])
                print(minn + maxn)
                break
            elif sum > number:
                startpos += 1
                break
        if sum == number:
            break


if __name__ == '__main__':
    errnum = find_number(numbers, 25)
    find_range(errnum, numbers)
