import datetime

with open('hardlopers.txt', 'w+') as file:
    datum = datetime.today().strftime("%a %d %b %Y")
    tijd = datetime.today().strftime("%T")
    hardloper = input('Vul naam van hardloper in')

    file.write(datum + ', ' + tijd + ', ' + hardloper)