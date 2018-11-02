nummer = 1
list = []
while (0 != nummer):
    nummer = int(input('Geef een getal'))
    list.append(nummer)
print('Er zijn ' + str(len(list) - 1) + ' getallen ingevoerd, de som is: ' + str(sum(list)) + '.')
