"""

8. Дано два цілих числа: D (день) і M (місяць), що визначають правильну дату невисокосного року.
Вивести значення D і M для дати, що передує зазначеній.
Єзелевич Ю.

"""


def date(x, y):
    x1 = x
    # Проверка для дня
    if x == 1:
        if y in [5, 7, 10, 12]:
            x = 30
        elif y in [1, 2, 4, 6, 8, 9, 11]:
            x = 31
        else:
            x = 28
    else:
        x -= 1
    # Проверка для месяца
    if x1 == 1:
        if y == 1:
            y = 12
        else:
            y -= 1
    return x, y


def proverka(m, d):
    while 12 < m or m < 0:
        m = int(input("Ошибка! Введите месяц (1-12) = "))

    if m in [1, 3, 5, 7, 8, 10, 12]:
        while 31 < d or d < 0:
            d = int(input("Ошибка! Введите день (1-31) ="))

    elif m in [4, 6, 9, 11]:
        while 30 < d or d < 0:
            d = int(input("Ошибка! Введите день (1-31) ="))

    else:
        while 28 < d or d < 0:
            d = int(input("Ошибка! Введите день (1-28) ="))

    d, m = date(d, m)
    print("Предыдущая дата = ", m, d)


if __name__ == '__main__':
    a = int(input("Введите месяц = "))
    b = int(input("Введите день = "))
    print(proverka(a, b))
