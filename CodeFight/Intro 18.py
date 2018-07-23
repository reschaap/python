from util import br


def palindromeRearranging(inputString):
    odd = 0
    characters = set(inputString)
    count = [(x, inputString.count(x)) for x in characters]
#    import pdb; pdb.set_trace()
    for x in count:
        if x[1]%2 != 0:
            odd += 1
            if odd > 1:
                return False, count, odd
        else:
            continue

    return True, count




# Client
s1 = "abbcabb" # True
s2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc" # False
s3 = "abbcabb" # True
s4 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa" # False
s5 = "z" # True

print(palindromeRearranging(s1))
br()
print(palindromeRearranging(s2))
br()
print(palindromeRearranging(s3))
br()
print(palindromeRearranging(s4))
br()
print(palindromeRearranging(s5))
br()