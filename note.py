import csv
import datetime

def add():
    with open('file.csv', "a", newline="", encoding='utf-8') as file:
        user = [input("Введите заголовок заметки: "), input("Введите тело новой заметки: "), datetime.datetime.now().strftime("%d-%m-%Y")]
        writer = csv.writer(file)
        writer.writerow(user)

def show():
    with open('file.csv', newline="", encoding='utf-8') as file:
        read = csv.reader(file)
        for row in read:
            print(row[0], " - ", row[1])


add()
#show()