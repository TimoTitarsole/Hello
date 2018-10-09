invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
uitvoer = sorted(list(map(int, invoer.split('-'))))

print(uitvoer)
print('Grootste getal: ' + str(max(uitvoer)) + ' en Kleinste getal: ' + str(min(uitvoer)))
print('Aantal getallen: ' + str(len(uitvoer)) + ' en Som van getallen: ' + str(sum(uitvoer)))
print('Gemiddelde: ' + str(sum(uitvoer) / len(uitvoer)))