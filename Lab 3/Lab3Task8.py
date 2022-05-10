"""

8. Дано дійсне A та ціле число N (> 0). Вивести 1 – A + A2 – A3 + ... + (–1)NAN.
Єзелевич Ю.

"""


def result(y, x) -> float:
    s = 0
    for i in range(x+1):
        s += pow(-y, i)
    return s


if __name__ == "__main__":
    a = float(input("A = "))
    n = int(input("N (N > 0)= "))
    while n <= 0:
        n = int(input("Ошибка! N (N > 0)= "))
    print(result(a, n))
