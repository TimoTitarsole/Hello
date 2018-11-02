cijferlijst = {
    'Peter': 2,
    'Luc': 8,
    'Etienne': 4,
    'Timo': 10,
    'Frenk': 7,
    'David': 9,
    'Brent': 7,
    'Frank': 2
}

for naam, cijfer in cijferlijst.items():
    if cijfer > 9:
        print(str(naam) + ': ' + str(cijfer))