import random

def monopolyworp():
    worpen = 0
    while worpen < 3:
        dobbel1 = random.randint(1, 7)
        dobbel2 = random.randint(1, 7)
        print(str(dobbel1) + " + " + str(dobbel2) + " = " + str(dobbel1 + dobbel2))

        if dobbel1 == dobbel2:
            worpen += 1
        if worpen == 3:
            print('ga naar de gevangenis')
        if dobbel1 != dobbel2:
            break

monopolyworp()