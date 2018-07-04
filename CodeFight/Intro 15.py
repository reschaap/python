from util import br


def addBorder(picture):
    padded = ['*{}*'.format(x) for x in picture]
    frame = [(len(picture[0]) + 2) * '*']
    return frame + padded + frame


# Client
picture = ["abc", "ded"]
picture_2 = ["wzy**"]

print(addBorder(picture))
br()
print(addBorder(picture_2))
