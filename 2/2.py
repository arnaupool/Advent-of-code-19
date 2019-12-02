def part1(noun, verb):
    with open('input.txt', 'r') as f:
        file = f.read().split(',')
        input = [int(i) for i in file]
    output = open('output.txt', 'w+')
    i = 0
    aux = 0
    input[1] = noun
    input[2] = verb

    while i < len(input):
        typ = input[i]
        num = input[i + 1]
        num2 = input[i + 2]
        loc = input[i + 3]

        if (typ == 99):
            break

        if (typ == 1):
            aux = input[num] + input[num2]
            input[loc] = aux

        if (typ == 2):
            aux = input[num] * input[num2]
            input[loc] = aux
        i = i + 4
        aux = 0
    output.write(str(input))
    output.close()
    return input[0]

def part2(res):
    for i in range(100):
        for j in range(100):
            if (res == part1(i, j)):
                print("Solution! i: " + str(i) + ' j: ' + str(j) + ' --> ' + str(i * 100 + j))


if __name__ == '__main__':
    part1(12, 2)
    part2(19690720)




    