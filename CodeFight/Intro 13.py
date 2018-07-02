def reverseParentheses(s):
    text = []
    reversed_text = ''
    while s:
        try:
            char = s.pop(0)
        except:
            s = [x for x in s]
            char = s.pop(0)
        if char == '(':
            rest = reverseParentheses(s)
            text = text + rest
        elif char == ')':
            text.reverse()
            return text
        else:
            text.append(char)
    return reversed_text.join(text)


# Client
s = "a(bc)de"
s_2 = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses(s))
print('\n')
print(reverseParentheses(s_2))
print('\n')

