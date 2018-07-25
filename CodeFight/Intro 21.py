from util import br

def isIPv4Address(inputString):
    input_list = inputString.split('.')
    correct = range(0, 256)
#    import pdb; pdb.set_trace()
    if len(input_list) != 4:
        return False
    else:
        try:
            for num in input_list:
                if int(num) in correct:
                    continue
                else:
                    return False
        except:
            return False
    return True


# Client
s1 = "172.16.254.1"
s2 = "172.316.254.1"
s3 = "1.1.1.1a"
s4 = "7283728"
s5 = "1.23.256.."

print(isIPv4Address(s1))
br()
print(isIPv4Address(s2))
br()
print(isIPv4Address(s3))
br()
print(isIPv4Address(s4))
br()
print(isIPv4Address(s5))
br()