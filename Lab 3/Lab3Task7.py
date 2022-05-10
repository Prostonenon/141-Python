"""

7. Дано ціле число N (> 2) і дві дійсні точки на числовій осі: A, B (A <B). Функція F (X) задана
формулою F (X) = 1 - sin (X). Вивести значення функції F в N рівновіддалених точках, що
утворюють розбиття відрізка [A, B]: F (A), F (A + H), F (A + 2H), ..., F (B).
Єзелевич Ю.

"""


import math


def foo(x):
    return 1 - math.sin(x)


if __name__ == "__main__":

    n = int(input("N (>2) = "))
    while n <= 2:
        n = int(input("Ошибка! N (>2) = "))

    a = float(input("A = "))

    b = float(input("B (>A) = "))
    while b <= a:
        b = float(input("Ошибка! B (>A) = "))

    h = (b - a) / n

    for i in range(n + 1):
        f = a + i * h
        print(foo(f))
