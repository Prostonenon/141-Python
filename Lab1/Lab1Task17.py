"""

17. Швидкість першого автомобіля V1 км/год, другого - V2 км/год, відстань між ними S км.
Визначити відстань між ними через T годин, якщо автомобілі спочатку рухаються назустріч один
одному. Дана відстань рівна модулю різниці початкової відстані і загального шляху, пройденого
автомобілями; загальний шлях = час · сумарна швидкість.

Єзелевич Ю.

"""


def distance(v1, v2, s, t) -> float:
    x = t * (v1 + v2)
    r = abs(s - x)
    return r


v1 = float(input("Скорость 1-го авто = "))
v2 = float(input("Скорость 2-го авто = "))
s = float(input("Расстояние между автомобилями = "))
t = float(input("Время = "))
print("Расстояние между авто спустя", t, "час(ов) = ", distance(v1, v2, s, t))
