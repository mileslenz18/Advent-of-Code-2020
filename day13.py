from helper_functions import getFileContent


def part_one(content):
    """Find the earliest bus you can take."""

    time = int(content[0])
    time_init = int(content[0])
    busses = content[1].split(',')
    busses = [int(bus) for bus in busses if bus != "x"]

    result = None
    while True:
        for bus in busses:
            if time % bus == 0:
                result = bus
                break

        if result:
            break

        time += 1

    time_to_wait = time - time_init

    result = time_to_wait * result

    return result


def part_two(content):
    """Find the earliest timestamp for all busses to depart with the offset."""

    time = int(content[0])
    busses = content[1].split(',')
    busses = [int(x) if x.isdigit() else x for x in busses]

    i, j = time, time
    correct = True
    while True:
        if j % 10000000000 == 0:
            print(j)
        for bus in busses:
            if bus == 'x':
                i += 1
                continue
            elif i % bus == 0:
                i += 1
            else:
                correct = False
                break
        if correct:
            break
        else:
            correct = True
            j += 1
            i = j

    return j


def main():
    content = getFileContent('input.txt')

    res1 = part_one(content)
    print(f'Part One: {res1}')

    res2 = part_two(content)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
