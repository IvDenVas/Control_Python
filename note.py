import csv
import datetime
import os
import operator

def add():# Если нет файла -> создает, если есть -> добавляет
    with open('file.csv', "a", newline="", encoding='utf-8') as file:
        user = [get_id() + 1, input("Введите заголовок заметки: "), input("Введите тело новой заметки: "), datetime.datetime.now().strftime("%Y-%m-%d")]
        writer = csv.writer(file, delimiter=";")
        writer.writerow(user)

def show():# Показать все заметки
    if os.path.exists('file.csv'):
        print("\nID - Тема заметки - Заметка - Дата создания/редактирования")
        with open('file.csv', newline="", encoding='utf-8') as file:
            read = csv.reader(file, delimiter=";")
            sortedlist = sorted(read, key=operator.itemgetter(3), reverse=False)
            for row in sortedlist:
                print(row[0], " - ", row[1], " - ", row[2], ' - ', row[3])
    else: print("Книга заметок пока пуста!")

def get_id():# Получение ID
    with open('file.csv', "r", newline="", encoding='utf-8') as file:
        read = csv.reader(file, delimiter=";")
        max_id = 0
        for row in read:
            if int(row[0]) > max_id:
                max_id = int(row[0])
    return max_id

def search_by_id():# Поиск по ID
    search_id = input("Введите ID нужной заметки: ")
    if check_id(search_id):
        with open('file.csv', newline="", encoding='utf-8') as file:
            read = csv.reader(file, delimiter=";")
            for row in read:
                if search_id in row[0]:
                    print(row[0], " - ", row[1], " - ", row[2], ' - ', row[3])
    else: print("Заметки с таким ID нет")

def search_by_name():# Поиск по имени
    search_name = input("Введите Заголовок нужной заметки: ")
    if check_str(search_name):
        with open('file.csv', newline="", encoding='utf-8') as file:
            read = csv.reader(file, delimiter=";")
            for row in read:
                if search_name in row[1]:
                    print(row[0], " - ", row[1], " - ", row[2], ' - ', row[3])
    else: print("Заметки с таким заголовком нет")


def remove():# Удалить заметку
    delete_id = input("Введите ID удаляемой заметки: ")
    if check_id(delete_id):
        while (True):
            temp = input("Подтвердите удаление - y/n: ")
            if temp == "y":
                with open('file.csv', newline="", encoding='utf-8') as file:
                    with open('temp.csv', "a", newline="", encoding='utf-8') as file1:
                        writer = csv.writer(file1, delimiter=";")
                        for row in csv.reader(file, delimiter=";"):
                            if delete_id not in row[0]:
                                writer.writerow(row)
                os.remove('file.csv') 
                os.rename('temp.csv', 'file.csv')
                print("Заметка удалена.")
                break
            elif temp == "n":
                print("Будьте аккуратнее)")
                break
            else:
                print("Неверный ввод!")
                continue
    else: print("Заметки с таким ID нет")

def edit():# Редактировать заметку
    edit_id = input("Введите ID изменяемой заметки: ")
    if check_id(edit_id):
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
    else: print("Заметки с таким ID нет")

def change_search():# Поиск по имени или ID
    while (True):
        change_user = input(" 1 - поиск по ID \n 2 - поиск по Заголовку\n 3 - выход из поиска\n Введите: ")
        if change_user == "1":
            search_by_id()
            break
        elif change_user == "2":
            search_by_name()
            break
        elif change_user == "3":
            break
        else:
            print("Неверный ввод!")
            continue  

def menu():# Меню
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
        elif action == "search":
            change_search()
        elif action == "exit":
            print("До свидания!")
            break
        else: 
            print("Такой команды нет!")
            continue

def check_id(inp):# Проверка наличия ID в файле
    with open('file.csv', newline="", encoding='utf-8') as file:
        temp = 0
        res = False
        read = csv.reader(file, delimiter=";")
        for row in read:
            if row[0] == inp:
                temp += 1
    if temp > 0:
        res = True
    return res

def check_str(inp):# Проверка наличия имени в файле
    with open('file.csv', newline="", encoding='utf-8') as file:
        temp = 0
        res = False
        read = csv.reader(file, delimiter=";")
        for row in read:
            if row[1] == inp:
                temp += 1
    if temp > 0:
        res = True
    return res

        
# if check_id(5): print("+")
# else: print("-")
            

# add()
# show()
#get_id()
# search_by_id()
# search_by_name()
# remove()
# edit()
menu()