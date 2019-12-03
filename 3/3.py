# One wire per line of text input


def manhattan(p1 : tuple, p2 : tuple):
    print('Doing manhattan...')
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part1(input):
    print('Doing part 1...')
    input = input.split(',')
    points = []
    x = 0
    y = 0

    for coord in input:
        dir = coord[:1]
        dist = int(coord[1:])
        if dir == 'R':
            for i in range(dist):
                x += 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))
        elif dir == 'L':
            for i in range(dist):
                x -= 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))
        elif dir == 'U':
            for i in range(dist):
                y += 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))
        elif dir == 'D':
            for i in range(dist):
                y -= 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))

    return points


def intersec(list1, list2):
    print('Doing intersec...')
    inter = []
    for elem1 in list1:
        for elem2 in list2:
            if (elem1 == elem2):
                inter.append(elem2)
    return inter


if __name__ == '__main__':
    origin = (0, 0)
    aux = 0
    closest = 10000
    file = open('input.txt', 'r')
    input = file.read().split()

    list1 = part1(input[0])
    list2 = part1(input[1])
    inter = intersec(list1, list2)
    #print(str(inter))
    for point in inter:
        aux = manhattan(origin, point)
        if (closest > aux):
            closest = aux
            #print(str(aux))
    print(str(closest))