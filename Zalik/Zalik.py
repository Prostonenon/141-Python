"""
Запитати у користувача код регіону

Отримати ЗВО з вказаного користувачем регіону
Зберегти всі дані у файл universities.csv у форматі csv

Збережіть ті ж дані у файл universities_<код регіону>.csv, наприклад universities_80.csv
Якщо регіон не зі списку доступних, то повідомити про це користувачеві у консолі

Відфільтруйте і збережіть таку інформацію про заклади Назви та англійські назви в файл ua_en.csv
Ускладніть програму з першого завдання наступним фільтром З формою фінансування Державна

Ускладніть програму з другого завдання можливістю фільтрування за будь-яким з наявних значень поля
Єзелевич Ю.
"""


import requests
import csv

code = str(input("Введите код региона: "))
r = requests.get(f"https://registry.edbo.gov.ua/api/universities/?ut=1&lc={code}&exp=json")

# Проверка на доступность региона, если регион не обслуживается или вообще не существует, нас кидает в цикл
while not r:
    code = str(input("Данный регион не обслуживается либо не существует!\n Введите код региона: "))
    r = requests.get(f"https://registry.edbo.gov.ua/api/universities/?ut=1&lc={code}&exp=json")

universities: list = r.json()

form_list = str("Державна, Приватна, Комунальна")
print(form_list)

form = str(input("Введите форму финансирования из списка выше: "))

# То же самое что и с регионом: цикл продолжается до тех пор, пока не введем форму из списка
while form not in form_list:
    form = str(input("Введена неверная форма финансирования! Введите форму из доступного списка: "))

filtered_data = [
    {
        k: row[k] for k in ["university_id", "university_name"]
    } for row in universities]

second_filtered_data = [
    {
        k: row[k] for k in ["university_name", "university_name_en", "university_financing_type_name"]
    } for k in ["university_financing_type_name"] for row in universities if row[k] == form]

with open("universities.csv", mode="w", encoding="UTF-8") as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

with open(f"universities_{code}.csv", mode="w", encoding="UTF-8") as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

with open("ua_en.csv", mode="w", encoding="UTF-8") as f:
    writer = csv.DictWriter(f, fieldnames=second_filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(second_filtered_data)
