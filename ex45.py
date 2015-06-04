class TextOutput(object):
    def __init__(self, text, width, height):
        self.text = text
        self.width = width
        self.height = height
        
#    def text_format(self):
#        """
#        Create TextFormat object. Call text_formatting method on the object to 
#        create the different border texts.
#        """
    
    def display_text(self):
        """
        Use the TextFormat.border_text_list to display the border texts.
        Get the len of text_format.border_text_list. Call the first border_text.
        If there are more use indexes to call the next border_texts. Use index+1
        or index-1 to call the next or the previous border_text. Use the len of 
        the list to show the appropriate options (Next, Back, End)
        """
        cls = 100 * '\n'
        text_format = TextFormat(self.text, self.width, self.height)
        text_format.text_formatting()

#        for border_texts in text_format.border_text_list:
#            print cls
#            for border_text in border_texts:
#
#                print border_text
#            answer = raw_input("Press enter to continue: ")

        total = len(text_format.border_text_list)
        end = False
        index = 0
        
        while end == False:
#            print cls
            print "len is ", total
            print "index is ", index
            for line in text_format.border_text_list[index]:
                print line
            
            if total == 1:
                answer = raw_input("Press 'e' to end. ")
                end = True
                continue
            elif index == 0:
                answer = raw_input("Press 'n' for next. Press 'e' to end. ")
                print answer
                if answer == 'n':
                    index += 1
                    continue
                else:
                    end = True
                    continue
            elif index > 0 and index < total - 1:
                answer = raw_input("""Press 'n' for next. Press 'b' for back.
                    Press 'e' to end. """)
                if answer == 'n':
                    index += 1
                    continue
                elif answer == 'b':
                    index -= 1
                    continue
                else:
                    end = True
                    continue
            elif index == total - 1:
                answer = raw_input("Press 'b' for back. Press 'e' to end.")
                if answer == 'b':
                    index -= 1
                    continue
                else:
                    end = True 
                    continue
            else:
                raise ValueError("len, index: ", total, index)
            

class TextFormat(object):
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
    def __init__(self, text, width, height):
        self.text = text
        self.width = width
        self.height = height
        self.words = self.text.split()
        self.border_text_list = []
        
    def text_formatting(self):
#        print "words :", self.words, "\n"
        
        while self.words != []:
            border_text = self.border_text()
#            print "border_text is : ", border_text
            self.border_text_list.append(border_text)
        
#        print "border_text_list is: ", self.border_text_list
    
    def border_text(self):
        border_char = '*'
        border_width = self.width + 4
        border_line = '{0:{1}^{2}}'.format('', border_char, border_width)
        space = '{0:{1}^{2}}'.format('', ' ', self.width)
        border_line_space = '{0} {1} {2}'.format(border_char, space, border_char)
        lines = []
        line = border_char + ' ' + self.words.pop(0)
        lines.append(border_line)
        lines.append(border_line_space)
    
    
        while len(lines) <= self.height and self.words != []:
            word = self.words.pop(0)
            
            new_lines = word.count('\\n')
            if new_lines > 0 and line != border_char:
                """
                Fill the current line with spaces up to the appropriate width 
                and append a border char. 
                Count the of '\\n' and add that number of 'border_line_space''s
                to 'lines'.
                """
                line = '{0: <{1}} {2}'.format(line, self.width + 2, border_char)
                lines.append(line)
                for i in range(0, new_lines):
                    lines.append(border_line_space) 
                line = border_char
                continue
            elif new_lines > 0 and line == border_char:
                """
                Just fill the current line with spaces up to the appropriate 
                width and append a border_char. Then start a new line with a 
                border_char.
                """
                line = '{0: <{1}} {2}'.format(line, self.width + 2, border_char)
                lines.append(line)
                line = border_char
                continue
#            else:
#                raise ValueError("new_lines, line : ", new_lines, line)
            
            test_width = line + ' ' + word
            if len(test_width) <= self.width:
                line = line + ' ' + word
            else:
                line = '{0: <{1}} {2}'.format(line, self.width + 2, border_char)
                lines.append(line)
                line = border_char + ' ' + word
    
        line = '{0: <{1}} {2}'.format(line, self.width + 2, border_char)
        lines.append(line)
        lines.append(border_line_space)
        lines.append(border_line)
        return lines