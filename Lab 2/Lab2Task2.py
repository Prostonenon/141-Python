"""

2. Дано три цілих числа. Знайти кількість додатних чисел в початковому наборі.
Єзелевич Ю.

"""


def foo(x, y, z):
    k = 0
    if x > 0:
        k = k + 1
    if y > 0:
        k = k + 1
    if z > 0:
        k = k+1
    return k


if __name__ == '__main__':
    a = int(input("Введіть перше число = "))
    b = int(input("Введіть друге число = "))
    c = int(input("Введіть третє число = "))
    print(foo(a, b, c))