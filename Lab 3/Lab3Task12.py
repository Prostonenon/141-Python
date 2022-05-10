"""

12. Дано ціле число N (> 0), яке є деяким ступенем числа 2: N = 2^K.
Знайти ціле число K — показник цієї ступені.
Єзелевич Ю.

"""


def power(x) -> int:
    for i in range(x):
        if x == pow(2, i):
            return i
    else:
        return -1


if __name__ == '__main__':
    n = int(input("2^K (n>0) = "))
    while n <= 0:
        n = int(input("Ошибка! 2^K (n>0) = "))

    while power(n) == -1:
        n = int(input("Целой степени не существует! 2^K (n>0) = "))
    else:
        print("Степень (K) = ", power(n))
