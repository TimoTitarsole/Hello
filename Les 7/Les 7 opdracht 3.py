with open('kaartnummers.txt', 'r') as file:
    i = regels = nummer = 0

    for regelnummer, line in enumerate(file):
        i += 1

        if int(line[:6]) > nummer:
            nummer = int(line[:6])
            regels = regelnummer
    file.close()

print('Deze file telt ' + str(i) + ' regels')
print('Het grootste kaartnummer is: ' + str(nummer) + ' en dat staat op regel ' + str(regels))