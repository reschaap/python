#def reverseParentheses(s):
#    sent = []
#    sect = []
#    reverse = ""
#    for char in s:
#        if char == '(':
#            sent.append(sect)
#            print("2: {}".format(sect))
#            sect = []
#        elif char == ')':
#            subs = ""
#            print("3: {}".format(sect))
#            sent.append(subs.join(reversed(sect)))
#
#            sect = []
#        else:
#            sect.append(char)
#            print("1: {}".format(sect))
#    if sect:
#        sent.append(sect)
#    else:
#        pass
#    return sent


def reverseParentheses(s):
    t = [x for x in s]
    text = []
    reversed = ''
    while t:
        char = t.pop(0)
        print ('char {}'.format(char))
        print('t {}'.format(t))
        if char == '(':
            reverse_text = parentheses(t)
            print('1 {}'.format(reverse_text))
            #text.append(reverse_text)
            text = text + reverse_text
            print('1b {}'.format(text))
        elif char == ')':
            print('2 {},{}'.format(t, text))
            continue
        else:
            text.append(char)
            print('3 {}'.format(text))
    print('4 {}'.format(text))
    return reversed.join(text)


def parentheses(t):
    text = []
    parentheses_text = ''
    while t:
        char = t.pop(0)
        print('char2 {}'.format(char))
        print('t2 {}'.format(t))
        if char == '(':
            rest = parentheses(t)
            print('11 {}'.format(rest))
            text = text + rest
            print('12 {}'.format(text))
        elif char == ')':
            text.reverse()
            print('22 {}'.format(text))
            #return parentheses_text.join(text)
            return text
        else:
            text.append(char)
            print('33 {}'.format(text))



# Client
s = "a(bc)de"
s_2 = "a(bcdefghijkl(mno)p)q"
#print(reverseParentheses(s))
print(reverseParentheses(s))
print('\n')
print(reverseParentheses(s_2))