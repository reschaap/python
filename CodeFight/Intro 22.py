from util import br


def avoidObstacles(inputArray):
    jump = None
    n = 2
#    import pdb; pdb.set_trace()
    index = len(inputArray)
    while not jump:
        for i in range(index):
            if i == index - 1 and inputArray[i]%n != 0:
                jump = n
            elif inputArray[i]%n == 0:
                n += 1
                break
            else:
                continue
    return jump




# Client
in1 = [5, 3, 6, 7, 9] # 4
in2 = [1000, 999] # 6
in3 = [19, 32, 11, 23] # 3

print(avoidObstacles(in1))
br()
print(avoidObstacles(in2))
br()
print(avoidObstacles(in3))
br()