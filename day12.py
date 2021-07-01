from helper_functions import getFileContent


def part_one(content):
    """Calculate the Manhattan distance."""

    directions = ["east", "south", "west", "north"]
    directionsIndex = 0
    position = {"north": 0, "east": 0}

    for instruction in content:

        if instruction[0] == "N":
            position["north"] += int(instruction[1:])
        elif instruction[0] == "S":
            position["north"] -= int(instruction[1:])
        elif instruction[0] == "E":
            position["east"] += int(instruction[1:])
        elif instruction[0] == "W":
            position["east"] -= int(instruction[1:])

        elif instruction[0] == "L":
            value = int(instruction[1:])
            if value == 90:
                directionsIndex -= 1
            elif value == 180:
                directionsIndex -= 2
            elif value == 270:
                directionsIndex -= 3

        elif instruction[0] == "R":
            value = int(instruction[1:])
            if value == 90:
                directionsIndex += 1
            elif value == 180:
                directionsIndex += 2
            elif value == 270:
                directionsIndex += 3

        elif instruction[0] == "F":
            if directionsIndex >= 0:
                index = directionsIndex % 4
            else:
                index = directionsIndex % -4
            facing = directions[index]

            if facing == "north":
                position["north"] += int(instruction[1:])
            elif facing == "east":
                position["east"] += int(instruction[1:])
            elif facing == "south":
                position["north"] -= int(instruction[1:])
            elif facing == "west":
                position["east"] -= int(instruction[1:])

    result = abs(position["north"]) + abs(position["east"])

    return result


def part_two(content):
    """Calculate distance between that location and starting position."""

    return None


def main():
    content = getFileContent('input.txt')

    res1 = part_one(content)
    print(f'Part One: {res1}')

    res2 = part_two(content)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
