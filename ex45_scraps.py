def textmargin(text, width):
    """
    'text' is a string that can contain new line characters and is delimited by
    triple qoutes. New line charactes have to added as '\\n' or they will not be 
    recognised. The words (including new line) in the string are added as 
    seperate strings in a list 'words'. These strings are then combined into new
    strings that are up to but not bigger than a fixed width 'width'. These are
    than stored in a list 'lines'. The list 'lines' can then be used to print the
    text.
    """
    words = text.split()
    lines = []
    line = words.pop(0)
    
    while words != []:
        word = words.pop(0)
        if word.rfind('\\n') != -1:
            word = word.replace('\\n', '\n')
            lines.append(line)
            line = word
            continue
        test_width = line + ' ' + word
        if len(test_width) <= width:
            line = line + ' ' + word
        else:
            lines.append(line)
            line = word
            
    lines.append(line)
    return lines

def text_border(text, width):
    """
    'text' is a string that can contain new line characters and is delimited by
    triple qoutes. New line charactes have to added as '\\n' or they will not be 
    recognised. The words (including new line) in the string are added as 
    seperate strings in a list 'words'. These strings are then combined into new
    strings that are up to but not bigger than a fixed width 'width'. These are
    than stored in a list 'lines'. The list 'lines' can then be used to print the
    text.
    To create a border around the text two new lines are created before the first
    and after the last line. These will be 4 characters longer than 'width'.Also
    every line will be preceded and ended with a character and a space and vice
    versa.
    Besides 'width' the 'height' argument can be used to limit how many lines
    are diplayed within one border. The user will be promted to press a key to 
    go to the next border if the text needs multiple borders to be displayed.
    """
    border_char = '*'
    border_width = width + 4
    border_line = '{0:{1}^{2}}'.format('', border_char, border_width)
    space = '{0:{1}^{2}}'.format('', ' ', width)
    border_line_space = '{0} {1} {2}'.format(border_char, space, border_char)
    
    words = text.split()
    print "words :", words, "\n"
    lines = []
    line = border_char + ' ' + words.pop(0)
    lines.append(border_line)
    lines.append(border_line_space)
    
    
    while words != []:
        word = words.pop(0)
        
        new_lines = word.count('\\n')
        if new_lines > 0 and line != border_char:
            """
            Fill the current line with spaces up to the appropriate width and 
            append a border char. 
            Count the of '\\n' and add that number of 'border_line_space''s to 
            'lines'.
            """
            line = '{0: <{1}} {2}'.format(line, width + 2, border_char)
            lines.append(line)
            for i in range(0, new_lines):
                lines.append(border_line_space) 
            line = border_char
            continue
        elif new_lines > 0 and line == border_char:
            """
            Just fill the current line with spaces up to the appropriate width
            and append a border_char. Then start a new line with a border_char.
            """
            line = '{0: <{1}} {2}'.format(line, width + 2, border_char)
            lines.append(line)
            line = border_char
            continue
            
        test_width = line + ' ' + word
        if len(test_width) <= width:
            line = line + ' ' + word
        else:
            line = '{0: <{1}} {2}'.format(line, width + 2, border_char)
            lines.append(line)
            line = border_char + ' ' + word
    
    line = '{0: <{1}} {2}'.format(line, width + 2, border_char)
    lines.append(line)
    lines.append(border_line_space)
    lines.append(border_line)
#    print "lines, ", lines, "\n"
    return lines