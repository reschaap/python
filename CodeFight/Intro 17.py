from util import br

def arrayChange(inputArray):
    change = 0
    for i, integer in enumerate(inputArray):
        if i == 0:
            continue
        elif integer > inputArray[i-1]:
            continue
        else:
            new_integer = inputArray[i-1] + 1
            change += abs(new_integer - integer)
            inputArray[i] = new_integer
    return change



# Client
array_1 = [1, 1, 1]
array_2 = [-1000, 0, -2, 0]
array_3 = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]

print(arrayChange(array_1))
br()
print(arrayChange(array_2))
br()
print(arrayChange(array_3))
br()