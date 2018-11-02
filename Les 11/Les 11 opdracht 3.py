import csv

lines = []

with open("score.csv", "r", newline="") as file:
    file_reader = csv.reader(file, delimiter=";")

    [lines.append("; ".join(row)) for row in file_reader]
    hoogstscore = max(lines[-2:]).split(";")

    name = hoogstscore[0]
    date = hoogstscore[1].replace(" ", "")
    score = hoogstscore[2].replace(" ", "")

    print("De hoogste score is: " + score + " op " + date + " behaald door " + name)