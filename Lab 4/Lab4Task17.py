"""

17. Дано список A, кількість елементів якого N. Сформувати новий список B того ж розміру за таким
правилом: елемент BK дорівнює середньому арифметичному елементів масиву A з номерами від 1 до к.
Єзелевич Ю.

"""


def list_b(x, o):
    b = list()
    for y in range(o):
        b.append(sum(x)/(y+1))
    return b


if __name__ == "__main__":
    n = int(input("Введите число элементов списка: "))
    a = list()
    for i in range(n):
        e = float(input(f"Введите {i+1}-й элемент списка A:"))
        a.append(e)
    print(f"Список А = {a}")
    print(f"список B = {list_b(a,n)}")
