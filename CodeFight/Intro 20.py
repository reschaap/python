def arrayMaximalAdjacentDifference(inputArray):
    diff = []
    for i, x in enumerate(inputArray):
        if i == 0:
            continue
        else:
            diff.append(abs(inputArray[i-1] - x))
    return max(diff)