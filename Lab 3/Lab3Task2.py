"""

2. Визначити, чи є задане натуральне число досконалим, тобто рівним сумі всіх своїх дільників, крім
самого цього числа (наприклад, число 6 досконале: 6 = 1 + 2 + 3).
Єзелевич Ю.

"""


def perfect(x) -> bool:
    s = 0
    for i in range(x//2):
        if x % (i+1) == 0:
            s += (i+1)
    if s == x:
        return True
    else:
        return False


if __name__ == '__main__':
    a = int(input("a = "))
    if perfect(a):
        print("Число досконале")
    else:
        print("Число не досконале")
