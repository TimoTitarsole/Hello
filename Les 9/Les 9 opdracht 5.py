def namen() -> print:
    namenlijst = {}
    naam = 0

    while naam != '':
        naam = input('Voer een naam in: ')
        if 1 < len(naam):
            if naam not in namenlijst:
                namenlijst[naam] = 1
            else:
                namenlijst[naam] += 1
    for naam, count in namenlijst.items():
        print(
            "Er {} {} student{} met de naam "
            .format('zijn' if 1 < count else 'is', count, 'en' if 1 < count else '')
            + naam
        )
    if 1 > len(namenlijst):
        print('Er zijn geen namen opgegeven')

namen()