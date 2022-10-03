import re
import csv

pattern_1 = r"(\+7|8)?\s*\(*(\d{3}){1}\)*[-\s]*(\d{3}){1}[-\s]*" \
            r"(\d{2}){1}[-\s]*(\d{2})(\s)*\(*(\w{3}.)*\s?(\d{4})*\)*"
repl_1 = r'+7(\2)\3-\4-\5\6\7\8'
pattern_2 = r"\s|,"
phonebook_list_1 = []

with open('phonebook_raw.csv', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    data = list(reader)
key_dict = data[0]

for row in data[1:]:
    string = ','.join(row) # преобразуем список в строку
    res_1 = re.sub(pattern_1, repl_1, string) # приводим номер телефона к заданному формату
    res_1_1 = res_1.split(',') # преобразуем строку в список
    res_2 = re.split(pattern_2, string) # преобразуем строку в список, в котором ФИО разделены
    res_3 = res_2[:3] + res_1_1[3:] # создаем новый список с данными требуемого формата
    phone_dic = {x: y for x, y in zip(key_dict, res_3)} # преобразуем список в словарь
    phonebook_list_1.append(phone_dic) # создаем список словарей

    # сортировка данных
phonebook_list_2 = []
for i in phonebook_list_1: # перебираем исходный список
    x = i['lastname']
    y = i['firstname']
    for j in phonebook_list_2: # перебираем новый список
        a = j['lastname']
        b = j['firstname']
        if a == x and b == y: # если человек с именем и фамилией уже есть в новом списке цикл прерывается
            if i['surname'] != '': # если поля с данными в новом списке не заполнены,
                j['surname'] = i['surname'] # они становятся равными значениям исходного списка,
            if i['organization'] != '': # которые сами имеют какое-то значение
                j['organization'] = i['organization']
            if i['position'] != '':
                j['position'] = i['position']
            if i['phone'] != '':
                j['phone'] = i['phone']
            if i['email'] != '':
                j['email'] = i['email']
            break
    else:
        phonebook_list_2.append(i) # если нет, данные добавляются в новый список

with open("phonebook.csv", "w", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0], lineterminator='\r')
    writer.writeheader()
    for row in phonebook_list_2:
        writer.writerow(row)






