import math

if __name__ == '__main__':
    input = open('input.txt', 'r')
    output = open('output.txt', 'w+')
    res = 0
    totalfuel = 0

    for elem in input.readlines():
        fuel = math.floor(int(elem) / 3) - 2
        res += fuel
        totalfuel += fuel
        while fuel >= 9:
            fuel = math.floor(fuel / 3) - 2
            totalfuel += fuel
        output.write('mass: ' + elem + ' - fuel: ' + str(totalfuel) + '\n')
    
    output.write(str(res))
    print('Result is ' + str(res) + ' and total fuel for it is ' + str(totalfuel))

    input.close()
    output.close()


        