studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(cijfers: list):
    antw = []

    for studenten in cijfers:
        antw.append(sum(studenten) / len(studenten))
    return antw


def gemiddelde_van_alle_studenten(cijfers: list):
    antw = sum(gemiddelde_per_student(cijfers)) / len(gemiddelde_per_student(cijfers))

    return antw


print(str(gemiddelde_per_student(studentencijfers)))
print(str(gemiddelde_van_alle_studenten(studentencijfers)))