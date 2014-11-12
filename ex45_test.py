import ex45
import test_texts

# print test_texts.central_corridor1
# text = test_texts.central_corridor2
# print text

lines = ex45.textmargin(test_texts.central_corridor1, 80)

for line in lines:
    print line