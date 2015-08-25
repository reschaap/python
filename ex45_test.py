import ex45
import test_texts

# print test_texts.central_corridor1
# text = test_texts.central_corridor2
# print text

# lines = ex45.text_border(test_texts.central_corridor1, 40)

# for line in lines:
#     print line

output = ex45.TextOutput(test_texts.central_corridor1, 30, 8, border_char='#')
#output.text_format()
output.display_text()

#border = ex45.TextFormat(test_texts.central_corridor1, 30, 10)
#border.text_formatting()
#print border.border_text_list

