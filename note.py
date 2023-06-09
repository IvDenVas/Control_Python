import csv

with open('file.csv', "a", newline="", encoding='utf-8') as file:
    user = [input("Введите заголовок заметки: "), input("Введите тело новой заметки: ")]
    writer = csv.writer(file)
    writer.writerow(user)


with open('file.csv', newline="", encoding='utf-8') as file:
    read = csv.reader(file)
    for row in read:
        print(row[0], " - ", row[1])
