from collections import Counter
from util import br


def palindromeRearranging(inputString):
    char_count = Counter(inputString)
    odd = [x for x in char_count.values() if x%2 != 0]
    return len(odd)<2




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