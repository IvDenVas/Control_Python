import csv
import datetime
import os
import operator

def add():
    with open('file.csv', "a", newline="", encoding='utf-8') as file:
        user = [get_id() + 1, input("Введите заголовок заметки: "), input("Введите тело новой заметки: "), datetime.datetime.now().strftime("%Y-%m-%d")]
        writer = csv.writer(file, delimiter=";")
        writer.writerow(user)

def show():
    print("\nID - Тема заметки - Заметка - Дата создания/редактирования")
    with open('file.csv', newline="", encoding='utf-8') as file:
        read = csv.reader(file, delimiter=";")
        sortedlist = sorted(read, key=operator.itemgetter(3), reverse=False)
        for row in sortedlist:
            print(row[0], " - ", row[1], " - ", row[2], ' - ', row[3])

def get_id():
    with open('file.csv', "r", newline="", encoding='utf-8') as file:
        read = csv.reader(file, delimiter=";")
        max_id = 0
        for row in read:
            if int(row[0]) > max_id:
                max_id = int(row[0])
    return max_id

def search_by_id():
    search_id = input("Введите ID нужной заметки: ")
    with open('file.csv', newline="", encoding='utf-8') as file:
        read = csv.reader(file, delimiter=";")
        for row in read:
            if search_id in row[0]:
                print(row[0], " - ", row[1], " - ", row[2], ' - ', row[3])

def search_by_name():
    search_name = input("Введите Заголовок нужной заметки: ")
    with open('file.csv', newline="", encoding='utf-8') as file:
        read = csv.reader(file, delimiter=";")
        for row in read:
            if search_name in row[1]:
                print(row[0], " - ", row[1], " - ", row[2], ' - ', row[3])

def remove():
    delete_id = input("Введите ID удаляемой заметки: ")
    with open('file.csv', newline="", encoding='utf-8') as file:
        with open('temp.csv', "a", newline="", encoding='utf-8') as file1:
            writer = csv.writer(file1, delimiter=";")
            for row in csv.reader(file, delimiter=";"):
                if delete_id not in row[0]:
                    writer.writerow(row)
    os.remove('file.csv') 
    os.rename('temp.csv', 'file.csv')
    print("Заметка удалена.")

def edit():
    edit_id = input("Введите ID изменяемой заметки: ")
    with open('file.csv', newline="", encoding='utf-8') as file:
        with open('temp2.csv', "a", newline="", encoding='utf-8') as file1:
            writer = csv.writer(file1, delimiter=";")
            for row in csv.reader(file, delimiter=";"):
                if edit_id not in row[0]:
                    writer.writerow(row)
                else:
                    user = [edit_id, row[1], input("Внесите изменение: "), datetime.datetime.now().strftime("%Y-%m-%d")]
                    writer.writerow(user)
    os.remove('file.csv') 
    os.rename('temp2.csv', 'file.csv')
    print("Заметка успешно изменена")

def menu():
    while (True):
        action = input("Введите необходимую команду:\n add - добавить новую заметку\n show - показать все заметки\n edit - редактировать заметку\n remove - удалить заметку\n search - поиск\n exit - выход: \n")
        if action == "add":
            add()
        elif action == "show":
            show()
        elif action == "edit":
            edit()
        elif action == "remove":
            remove()
        elif action == "search_id":
            search_by_id()
        elif action == "search_name":
            search_by_name()
        elif action == "exit":
            print("До свидания!")
            break
        else: 
            print("Такой команды нет!")
            continue

# add()
# show()
#get_id()
# search_by_id()
# search_by_name()
# remove()
# edit()
menu()