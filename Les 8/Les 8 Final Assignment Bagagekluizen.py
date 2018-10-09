def file_len(file_name):
    i = [0]
    with open(file_name) as file:
        for i in enumerate(file, 1):
            pass
    return i[0]

def toon_aantal_kluizen_vrij():
    print('Er zijn nog ' + str(12 - file_len('kluizen.txt')) + ' kluizen vrij.')


def nieuwe_kluis():
    with open('kluizen.txt', 'r') as file:
        gebruikte_kluizen = []
        for line in file:
            gebruikte_kluizen.append(int(line.split(';')[0]))

    kluisnummer = int(input('Vul het nummer van de kluis in:'))

    if kluisnummer not in gebruikte_kluizen and 0 < kluisnummer < 13:
        nieuw_kluisnummer = kluisnummer
    else:
        print('deze kluis is al in gebruik')
        return False

    nieuw_wachtwoord = input('Vul een nieuw wachtwoord van minimaal 4 tekens in:')
    if len(nieuw_wachtwoord) < 4:
        print('Het gekozen wachtwoord is te kort!')
    else:
        with open('kluizen.txt', 'a') as file:
            file.write(str(nieuw_kluisnummer) + ';' + str(nieuw_wachtwoord) + '\n')
            kluis = str(kluisnummer)
            print('U heeft nu kluis' + ' ' + kluis + '.')


def kluis_openen():
    kluisnummer = input('Vul uw kluisnummer in:')

    with open('kluizen.txt', 'r') as file:
        for line in file:
            if int(kluisnummer) == int(line.split(';')[0]):
                wachtwoord = input('Vul uw wachtwoord in:')
                if wachtwoord == line.split(';', 1)[1].rstrip():
                    print('Uw kluis wordt nu geopend')

                    return True
                print('Wachtwoord komt niet overeen.')

                return False
    print('Kluis is niet in gebruik.')

    return False


print("1: Ik wil weten hoeveel kluizen nog vrij zijn\n" \
         "2: Ik wil een nieuwe kluis\n" \
         "3: Ik wil even iets uit mijn kluis halen\n")

keuze = int(input('Wat is uw keuze?'))

if keuze == 1:
    toon_aantal_kluizen_vrij()
if keuze == 2:
    nieuwe_kluis()
if keuze == 3:
    kluis_openen()
else:
    print('Er zijn maar 3 opties! Kies 1 van de 3 opties!')