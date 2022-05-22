"""

2. Дано рядок, що містить повне ім'я файлу (наприклад, C:\WebServers\home\testsite\www\myfile.txt).
Виділіть з цього рядка ім'я файлу без розширення.
Єзелевич Ю.

"""


from os import path


def simple_name(name):
    name = path.basename(name)
    name = path.splitext(name)[0]
    return name


if __name__ == "__main__":
    fullname = str(input("Введите полное имя файла "))
    print(simple_name(fullname))

