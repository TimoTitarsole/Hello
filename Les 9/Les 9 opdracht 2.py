word = ''
while True:
    word = input('Geef een string van 4 letters:')

    if 4 == len(word):
        print('Inlezen van correcte string: ' + word + ' is geslaagd.')
        break
    elif 1 == len(word):
        print(word + ' heeft ' + str(len(word)) + ' letter.')
    else:
        print(word + ' heeft ' + str(len(word)) + ' letters.')