def convert(celcius):
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit

def table():
    for i in range(-30, 41, 10):
        print(convert(i), "        ", i)
print('F', "           ", 'C')
print(table())