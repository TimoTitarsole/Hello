import csv

producten = [[121, 'ABC123', 'Highlight pen', 231, 0.56],
             [123, 'PQR678', 'Nietmachine', 587, 9.99],
             [128, 'ZYX163', 'Bureaulamp', 34, 19.95],
             [137, 'MLK709', 'Monitorstandaard', 66, 32.50],
             [271, 'TRS665', 'Ipad hoes', 155, 19.01]]

with open('producten.csv', 'w+', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["Artikelnummer", "Artikelcode", "Naam", "Voorraad", "Prijs"])
    for product in producten:
        csv_writer.writerow(product)

lines = []
with open("producten.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    [lines.append(line) for line in csv_reader]

    minstvoorraad = 'unset'
    hoogsterpijs = 0
    totaal = 0
    duurste = []

    for line in lines[1:]:
        count = int(line[3])

        if minstvoorraad == 'unset':
            minstvoorraad = count
            lowest_count_product = line
        elif minstvoorraad > count:
            minstvoorraad = count
            lowest_count_product = line

        if float(line[4]) > hoogsterpijs:
            hoogsterpijs = float(line[4])
            duurste = line
        totaal += int(line[3])

    print('Het duurste artikel is', duurste[2], 'en die kost', duurste[4])
    print("Er zijn slechts", lowest_count_product[3], "exemplaren in voorraad van het product met nummer", lowest_count_product[0])
    print('In totaal hebben wij', totaal, 'producten in ons magazijn liggen')
