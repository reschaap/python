def textmargin(text, length):
    """
    'text' is a string that can contain newline characters and is delimited by
    triple qoutes. The words (including newline) in the string are added as 
    seperate strings in a list 'words'. These strings are then combined into new
    strings that are up to but not bigger than a fixed length 'length'. These are
    than stored in a list 'lines'. The list 'lines' can than be used to print the
    text.
    """
    words = text.split(' ')
    print "words, ", words
    lines = []
    line = words.pop(0)
    
    while words != []:
        word = words.pop(0)
        test_line = line + ' ' + word
        if len(test_line) <= length:
            line = line + ' ' + word
        else:
            lines.append(line)
            line = word
            
    lines.append(line)
    return lines