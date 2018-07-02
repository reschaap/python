from itertools import islice
from util import br


def alternatingSums(a):
    slice_a = islice(a, None, None, 2)
    slice_b = islice(a, 1, None, 2)
    return sum(slice_a), sum(slice_b)


# Client

a = [50, 60, 60, 45, 70]
a_1 = [80]
a_2 = [100, 50]
print(alternatingSums(a))
br()
print(alternatingSums(a_1))
br()
print(alternatingSums(a_2))
br()
