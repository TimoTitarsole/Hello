from datetime import datetime
import csv

achternaam = None
current_date = datetime.today().strftime("%a %d %b %Y")
current_time = datetime.today().strftime("%H:%M")
formatted_date = current_date + ' at ' + current_time

with open('login.csv', 'w', newline='') as file:
    file_writer = csv.writer(file, delimiter=';',)

    while not achternaam == 'einde':
        achternaam = input('Voer uw achternaam in: ')

        if achternaam != 'einde':
            initialen = input('Voer de voorletters van uw naam in: ')
            geboortedatum = input('Voer uw geboortedatum in: ')
            email = input('Voer uw e-mailadres in: ')
            file_writer.writerow([formatted_date] + [initialen, achternaam, geboortedatum, email])