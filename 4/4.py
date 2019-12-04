def comprov1(number):
    repeat = 0
    anterior = None
    flag = False
    repeatN = 0
    numberList = [int(i) for i in str(number)]
    for current in numberList:
        if (anterior is not None):
            if (current == anterior):
                if (repeat == 0):
                    repeat = current
                    repeatN = 1
                    flag = True
                else:
                    if (current != repeat):
                        repeat = 0
                    else:
                        repeatN += 1
                        if (repeatN > 1):
                            #print('Number: ' + str(number) + ' - i: ' + str(current) + ' - Reps: ' + str(repeatN) + ' - Repeat number: ' + str(repeat))
                            return False                        
            else:
                if (current < anterior):
                    return False
        else:
            pass
            #repeat = current
        anterior = current
    if (flag):
        return True
    return False

if __name__ == "__main__":
    accepted = open('accepted.txt', 'w+')
    notaccepted = open('notaccepted.txt', 'w+')
    npass = 0
    for i in range(172930, 683082):
        if (comprov1(i)):
            npass += 1
            accepted.write('Accepted: ' + str(i) + '\n')
        notaccepted.write('Not accepted: ' + str(i) + '\n')
    print(str(npass))

