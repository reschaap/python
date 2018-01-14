def allLongestStrings(inputArray):
    long_string = [""]
    for item in inputArray:
        if len(item) == len(long_string[0]):
            long_string.append(item)
        elif len(item) > len(long_string[0]):
            long_string = [item]
        else:
            continue
    return long_string



#client
array1 = ["aba", "aa", "ad", "vcd", "aba"]
array2 = ["abc", "eeee", "abcd", "dcd"]

print(allLongestStrings(array1))
print(allLongestStrings(array2))