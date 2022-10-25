from find import find_last_id
from logg import log_add
import csv


def add_line(lis, fail):
    with open(fail, 'a', newline='', encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(lis)
    log_add(fail,lis[0])


def add_new_worker():
    file = "Psih_palata/Personal.csv"
    new_worker_profil = []
    new_worker_profil = add_id(new_worker_profil, file)
    new_worker_profil = add_name(new_worker_profil, 1)
    new_worker_profil = add_last_name(new_worker_profil, 1)
    new_worker_profil = add_post(new_worker_profil)
    new_worker_profil = add_phone(new_worker_profil)
    new_worker_profil = add_parking_nam(new_worker_profil)
    new_worker_profil = add_ward_id(new_worker_profil)
    add_line(new_worker_profil, file)


def add_new_ward():
    file = "Psih_palata/Patients.csv"
    new_ward_profil = []
    new_ward_profil = add_id(new_ward_profil, file)
    new_ward_profil = add_name(new_ward_profil, 0)
    new_ward_profil = add_last_name(new_ward_profil, 0)
    new_ward_profil = add_diagnosis(new_ward_profil)
    new_ward_profil = add_room(new_ward_profil)
    new_ward_profil = add_size(new_ward_profil)
    new_ward_profil = add_status(new_ward_profil)
    add_line(new_ward_profil, file)


def add_id(lis, file):
    lis.append(find_last_id(file)+1)
    return lis


def add_name(lis, typ):
    if typ == 1:
        typ = "сотрудника"
    else:
        typ = "пациента"
    lis.append(input(f"Введите имя новокго {typ}: ").strip().capitalize())
    return lis


def add_last_name(lis, typ):
    if typ == 1:
        typ = "сотрудника"
    else:
        typ = "пациента"
    lis.append(input(f"Ввкдите фамилию нового {typ}: ").strip().capitalize())
    return lis


def add_post(lis):
    lis.append(input(f"{lis[2]} {lis[1]} в должности: ").strip().capitalize())
    return lis


def add_phone(lis):
    lis.append(input(f"{lis[2]} {lis[1]} телефон: ").strip().capitalize())
    return lis


def add_parking_nam(lis):
    lis.append(input(f"{lis[3]} {lis[2]} паркуется на месте №: "))
    return lis


def add_ward_id(lis):
    lis.append(input(f"{lis[3]} {lis[2]} опекает пациетна с id(если есть): "))
    return lis


def add_diagnosis(lis):
    lis.append(input(f"Опишите диагноз: "))
    return lis


def add_room(lis):
    lis.append(input(f"Номер палаты: "))
    return lis


def add_size(lis):
    lis.append(input(f"Размер смирительной рубашки: "))
    return lis


def add_status(lis):
    lis.append(input(f"Состояние (статус): "))
    return lis


# lower(): переводит строку в нижний регистр
# capitalize(): переводит в верхний регистр первую букву только самого первого слова строки
