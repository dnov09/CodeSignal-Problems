def adjacentElementsProduct(inputArray):
    rv = []
    count = 0
    while count < (len(inputArray) - 1):
        rv.append(inputArray[count] * inputArray[count + 1])
        count += 1
    return max(rv)
