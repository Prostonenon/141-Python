"""

17. Дано ціле число N (> 1). Знайти найменше ціле число K, при якому виконується нерівність 3K> N.
Єзелевич Ю.

"""


def num(x) -> int:
    for i in range(x):
        if 3*i > x:
            return i


if __name__ == "__main__":
    n = int(input("N (N>1) = "))
    while n <= 1:
        n = int(input("Ошибка! N (N>1) = "))
    print(num(n))
