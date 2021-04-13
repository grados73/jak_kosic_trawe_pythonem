print("Let's begin!")
spam = ['jablka' , 'banany', 'pomarancze', 'tofu', 'koty']

print(spam[1])
def funkcja(spam):
    text = ''
    for i in range(len(spam)-2):
        text = text + spam[i] +', '
    text += spam[len(spam)-2]
    text += ' i '
    text += spam[len(spam)-1]
    return text

print(funkcja(spam))

