
def ticker(filename: str):
    tickers = {}

    with open(filename, 'r') as file:
        for line in file:
            split_line = line.strip().split(':')
            dict_key = split_line[0]
            dict_value = split_line[1]
            tickers[dict_key] = dict_value
        return tickers

def vraagsymbol(filename: str, bedrijfsnaam: str):
    tickers = ticker(filename)
    if bedrijfsnaam in tickers:
        return 'Ticker symbol:' + ' ' + tickers[bedrijfsnaam]
    return 'Bedrijfsnaam "' + bedrijfsnaam + '" komt niet overeen met een symbol.'

def vraagnaam(filename: str, tickersymbol: str):
    tickers = ticker(filename)
    for naam, symbol in tickers.items():
        if symbol == tickersymbol:
            return 'Bedrijfsnaam:' + ' ' + naam
    return 'symbol "' + tickersymbol + '" komt niet overeen met een bedrijfsnaam'

print("1: Ik wil een symbool opvragen\n" "2: Ik wil een bedrijfsnaam opvragen")
keuze = (input('Wat wilt u doen?'))

if keuze == '1':
    bedrijfsnaam = (input('Vul een bedrijfsnaam in: '))
    print(vraagsymbol('tickersymbols.txt', bedrijfsnaam))
elif keuze == '2':
    tickersymbol = input('Vul een tickersymbol in: ')
    print(vraagnaam('tickersymbols.txt', tickersymbol))
else:
    print('Kies uit 1 van de 2 keuzes!')