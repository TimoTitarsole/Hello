lijst1 = eval(input("Geef lijst met minimaal 10 strings: "))
lijst2 = []


for word in lijst1:
    if len(word) == 4:
        lijst2.append(word)


print('De nieuw-gemaakte lijst met alle vier-letter strings is:' + str(lijst2))