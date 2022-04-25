"""

12. Дано чотири цілих числа, одне з яких відмінно від трьох інших, рівних між собою. Вивести
порядковий номер цього числа
Єзелевич Ю.

"""


def one_of_four(m, n, p, k) -> int:
    if m != n == p == k:
        return 1
    elif n != m == p == k:
        return 2
    elif p != m == n == k:
        return 3
    elif k != m == n == p:
        return 4
    else:
        return 0


if __name__ == '__main__':
    print("Введите 4 целых числа, 3 из которых равны между собой")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    while one_of_four(a, b, c, d) == 0:
        print("Ошибка! Введите целых 4 числа, 3 из которых равны между собой")
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        d = int(input("d = "))
    print("число №", one_of_four(a, b, c, d))
