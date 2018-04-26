def sortByHeight(a):
    people = [x for x in a if x != -1]
    people.sort()
    for index, item in enumerate(a):
        if item != -1:
            a[index] = people.pop(0)
        else:
            continue
    return a





#Client
a = [-1, 150, 190, 170, -1, -1, 160, 180]
result = sortByHeight(a)
print(result)