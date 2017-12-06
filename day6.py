# http://adventofcode.com/2017/day/6
# part1
import copy

input = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]


def isInList(listOfPastStates, input, count):
    isFound = 0
    for index in range(len(listOfPastStates)):
        # each new line is potentially the same
        isFound = 1
        for index2 in range(len(input)):
            if listOfPastStates[index][index2] != input[index2]:
                isFound = 0

        if isFound == 1:
            print('Same input is found at the index:', index, 'count is', count, 'the cycle is:', count - index)
            return isFound

    return isFound


count = 0
isExistingSateFound = 0
listOfPastStates = []
while isExistingSateFound == 0:
    # store the current state of input
    listOfPastStates.append(copy.deepcopy(input))

    # get highest bank
    maxBank = input[0]
    maxBankIndex = 0
    for index in range(len(input)):
        if input[index] > maxBank:
            maxBank = input[index]
            maxBankIndex = index

    # distribute this maxBank
    position = maxBankIndex
    input[maxBankIndex] = 0
    while maxBank > 0:
        if position + 1 == len(input):
            position = 0
        else:
            position += 1
        input[position] += 1
        maxBank -= 1

    count += 1
    isExistingSateFound = isInList(listOfPastStates, input, count);

print(count)
