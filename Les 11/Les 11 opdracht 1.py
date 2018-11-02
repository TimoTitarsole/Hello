personen = input('Hoeveel mensen gaan mee?')
try:
    4356 / int(personen)

    if 0 > int(personen):
        print('Aantal = ' + personen + ' - Negatieve getallen zijn niet toegestaan!')
    else:
        print('4356 / ' + personen + ' = ' + str(4356 / int(personen)))
except ZeroDivisionError:
    print('Aantal = ' + personen + ' - Delen door nul kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except BaseException:
    print('Onjuiste invoer!')

