# One wire per line of text input


def manhattan(p1 : tuple, p2 : tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def manhattan2(p1 : tuple):
    return abs(p1[0]) + abs(p1[1])


def part1(input):
    print('Doing part 1...')
    input = input.split(',')
    points = []
    pointsandsteps = []
    x = 0
    y = 0
    steps = 0

    for coord in input:
        dir = coord[:1]
        dist = int(coord[1:])
        if dir == 'R':
            for i in range(dist):
                x += 1
                steps += 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))
                    pointsandsteps.append((x, y, steps))
        elif dir == 'L':
            for i in range(dist):
                x -= 1
                steps += 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))
                    pointsandsteps.append((x, y, steps))
        elif dir == 'U':
            for i in range(dist):
                y += 1
                steps += 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))
                    pointsandsteps.append((x, y, steps))
        elif dir == 'D':
            for i in range(dist):
                y -= 1
                steps += 1
                if ((x, y) in points):
                    pass
                else:
                    points.append((x, y))
                    pointsandsteps.append((x, y, steps))
    #return points
    print('part1 done!')
    return pointsandsteps


def intersec1(list1, list2):
    print('Doing intersec1... - ', len(list1), len(list2))
    inter1 = []
    for elem1 in list1:
        for elem2 in list2:
            if (elem1 == elem2):
                inter1.append(elem2)
    print('intersec1 done!')
    return inter1

def intersec2(list1, list2):
    print('Doing intersec2... - ', len(list1), len(list2))
    inter2 = []
    for elem1 in list1:
        for elem2 in list2:
            if (elem1[0] == elem2[0] and elem1[1] == elem2[1]):
                inter2.append((elem1[0], elem1[1], elem1[2] + elem2[2]))
    print('intersec2 done!')
    return inter2

def stepscalc(inter):
    print('Doing stepscalc...')
    min = 1000000000000
    for point in inter:
        if (point[2] < min):
            min = point[2]
    print('stepscalc done!')
    return min

def closest(inter):
    origin = (0, 0)   
    aux = 0
    closest = 1000000000000
    for point in inter:
        aux = manhattan(origin, point)
        if (closest > aux):
            closest = aux
    print(str(closest))

if __name__ == '__main__': 
    file = open('input.txt', 'r')
    input = file.read().split()

    list1 = part1(input[0])
    list2 = part1(input[1])
    inter = intersec2(list1, list2)

    print(str(stepscalc(inter)))
    #closest(inter)

    