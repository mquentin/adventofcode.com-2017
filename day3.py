# http://adventofcode.com/2017/day/3
# part1:

# 1) get the distances form 1 to all the elements on the cross centered in 1
# need 277730 squares: square root of 277678 = 526.95, 527*527 = 277729
nbSquares = 277730

listSquareDistances = [0] * (nbSquares + 1)

# fill grid with the max distance for all elements and min distance for the cross elements
i = 3
for index in range(1, nbSquares):
    # max element
    if index == i * i - ((i - 1) * 0):
        listSquareDistances[index] = i - 1
    if index == i * i - ((i - 1) * 1):
        listSquareDistances[index] = i - 1
    if index == i * i - ((i - 1) * 2):
        listSquareDistances[index] = i - 1
    if index == i * i - ((i - 1) * 3):
        listSquareDistances[index] = i - 1

    # min element
    if index == i * i - ((i - 1) * 0) - i // 2:
        listSquareDistances[index] = i // 2
    if index == i * i - ((i - 1) * 1) - i // 2:
        listSquareDistances[index] = i // 2
    if index == i * i - ((i - 1) * 2) - i // 2:
        listSquareDistances[index] = i // 2
    if index == i * i - ((i - 1) * 3) - i // 2:
        listSquareDistances[index] = i // 2

    # next square layer
    if index == i * i:
        i += 2

# fill the 'in between' min and max element
i = 3
for index in range(1, nbSquares):
    # here you are not a max or a min
    if listSquareDistances[index] == 0:

        # get your closest max and min
        indexMax = 0
        dMax = i - 1
        indexMin = 0
        dMin = i // 2
        for index2 in range(1, i // 2):
            # found a min ->
            if index + index2 <= nbSquares and listSquareDistances[index + index2] == dMin:
                listSquareDistances[index] = dMin + index2
                break
            # found a max ->
            elif index + index2 <= nbSquares and listSquareDistances[index + index2] == dMax:
                listSquareDistances[index] = dMax - index2
                break
            # found a min <-
            elif listSquareDistances[index - index2] == dMax:
                listSquareDistances[index] = dMax - index2
                break
            # found a max <-
            elif listSquareDistances[index - index2] == dMax:
                listSquareDistances[index] = dMax - index2
                break

    # next square layer
    if index == i * i:
        i += 2

    if index < 50:
        print(index, listSquareDistances[index])


# should be 31
print('d 1024', listSquareDistances[1024])

# result
print('d 277678', listSquareDistances[277678])
