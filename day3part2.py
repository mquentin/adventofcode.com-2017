# http://adventofcode.com/2017/day/3
# part2:
import numpy as np

# printable example
# mSize = 7

# required matrix size
mSize = 11

m = np.zeros(shape=(mSize, mSize))
mIndex = np.zeros(shape=(mSize, mSize))
m[mSize // 2, mSize // 2] = 1

squareLayer = 0
i = mSize // 2
j = mSize // 2
for index in range(0, mSize * mSize):
    mIndex[i, j] = index

    # set the value of the matrix
    if index > 0:
        if i > 0 and j > 0:
            m[i, j] += m[i - 1, j - 1]

        if i > 0:
            m[i, j] += m[i - 1, j]

        if j > 0:
            m[i, j] += m[i, j - 1]

        if i < mSize - 1:
            m[i, j] += m[i + 1, j]

        if j < mSize - 1:
            m[i, j] += m[i, j + 1]

        if i < mSize - 1 and j < mSize - 1:
            m[i, j] += m[i + 1, j + 1]

        if i > 0 and j < mSize - 1:
            m[i, j] += m[i - 1, j + 1]

        if j > 0 and i < mSize - 1:
            m[i, j] += m[i + 1, j - 1]


    if m[i, j] > 277678:
        print('result is:', m[i, j])
        break

    # Get the next square
    # right
    if i == j and j == mSize // 2 + squareLayer:
        # case where we increase the square layer
        squareLayer += 1
        j += 1

    elif i == mSize // 2 + squareLayer and j < mSize // 2 + squareLayer:
        j += 1


    # up
    elif j == mSize // 2 + squareLayer and i > mSize // 2 - squareLayer:
        i -= 1


    # left
    elif i == mSize // 2 - squareLayer and j > mSize // 2 - squareLayer:
        j -= 1


    # down
    elif i == j and j < mSize // 2:
        i += 1

    elif j == mSize // 2 - squareLayer and i < mSize // 2 + squareLayer:
        i += 1

print('Matrix of indexes')
print(mIndex)
print('Result matrix')
print(m)
