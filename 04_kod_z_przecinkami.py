print("Let's begin!")
spam = ['jablka' , 'banany', 'pomarancze', 'tofu', 'koty']

print(spam[1])
def funkcja(spam):
    text = ''
    for i in range(len(spam)):
        if i == (len(spam)-2):
            text = text + spam[i] + ' i '
        else:
            text = text + spam[i] + ', '
    return text

print(funkcja(spam))

