def kwadraten_som(grondgetallen):
    antwoord =[]
    for getal in grondgetallen:
        if getal > 0:
            antwoord.append(getal **2)
    print(sum(antwoord))


kwadraten_som([4, 5, 3, -81])
