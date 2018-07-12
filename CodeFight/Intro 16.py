from util import br


def areSimilar(a, b):
    if a == b:
        return True
    x = None
    y = None
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            if x and y:
                return False
            elif x:
                y = (a[i], b[i])
            else:
                x = (a[i], b[i])
    return x[0] == y[1] and x[1] == y[0]




# Client
a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]

a_1 = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b_1 = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

print(areSimilar(a, b))
br()
print(areSimilar(a_1, b_1))
