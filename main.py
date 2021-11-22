import math
import random


def exercise1_1():
    import math
    print(round(math.pi, 2))


def exercise1_2():
    import math
    print(round(math.e, 1))


def exercise1_3():
    y = input("Введіть число")
    print(f"Ви ввели число {y}")


def exercise1_4():
    y = input("Введіть число")
    print(f"{y} - Вот какое число вы ввели")


def exercise1_5():
    print(1, 13, 49)


def exercise1_6():
    print("5  5  5")


def exercise1_7():
    chislo1 = input()
    chislo2 = input()
    chislo3 = input()
    print(f"{сhislo1}  {сhislo2}  {сhislo3}")


def exercise1_8():
    chislo1 = input()
    chislo2 = input()
    chislo3 = input()
    chislo4 = input()
    print(f"{сhislo1}  {сhislo2}  {сhislo3} {сhislo4}")


def exercise1_9():
    print("50\n10")


def exercise1_10():
    print("5\n10\n21")


def exercise1_11():
    chislo1 = input()
    chislo2 = input()
    chislo3 = input()
    chislo4 = input()
    print(f"{chislo1}\n{chislo2}\n{chislo3}\n{chislo4}\n")


def exercise1_12a():
    print("5 10\n7 см")


def exercise1_12b():
    t = int(input())
    v = int(input())
    print(f"100 {t} \n1949 {v}")


def exercise1_12c():
    x = int(input())
    y = int(input())
    print(f"{x} 25\n{x} {y}")


def exercise1_13a():
    print("2 кг\n13 17")


def exercise1_13b():
    chislo1 = int(input())
    chislo2 = int(input())
    print(f"{chislo1} 1\n19 {chislo2}")



def exercise1_13c():
    x = int(input())
    y = int(input())
    print(f"{x} {y}\n5 {y}")


def exercise1_14():
    import math
    x = int(input("Введіть x"))
    a = int(input("Введіть a"))
    n = int(input("Введіть n"))
    y = int(input("Введіть y"))
    b = int(input("Введіть b"))
    num_1 = 2 * x
    num_2 = math.sin(x)
    num_3 = a * a
    num_4 = math.sqrt(x)
    num_5 = math.fabs(n)
    num_6 = 5 * math.cos(y)
    num_7 = -7.5 * a * a
    num_8 = 3 * math.sqrt(x)
    num_9 = math.sin(a) * math.cos(b) + math.sin(b) * math.cos(a)
    num_10 = a * math.sqrt(2 * b)
    num_11 = 3 * math.sin(2 * a) * math.cos(3 * b)
    num_12 = -5 * math.sqrt(x + math.sqrt(y))


def exercise1_15():
    import math
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    c = int(input("Введіть c"))
    x = int(input("Введіть x"))
    m = int(input("Введіть m"))
    n = int(input("Введіть n"))
    num_a = -1 / pow(x, 2)
    num_b = a / (b * c)
    num_c = (a / b) * c
    num_d = (a + b) / 2
    num_e = 5.45 * ((a + 2 * b) / (2 - a))
    num_f = -b + math.sqrt(pow(b, 2) - 4 * a * c) / (2 * a)
    num_g = (-b + (1 / a)) / (2 / c)
    num_h = 1 / (1 + (a + b) / 2)
    num_i = 1 / (1 + 1 / (2 + 1 / (2 + 3 / 5)))
    num_j = pow(pow(m, n), 2)

def exercise1_16():
    import math
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    c = int(input("Введіть c"))
    d = int(input("Введіть d"))
    r = int(input("Введіть r"))
    x = int(input("Введіть x"))
    num_a = a / b / c
    num_b = a * b / c
    num_c = a / b * c
    num_d = a + b / c
    num_e = a + b / c
    num_f = a + b / b + c
    num_g = a + b / b + c
    num_h = a * math.sin(b)
    num_i = 1/2 * a * b * math.sin(x)
    num_j = 2 * b * c * math.cos(a) / 2 / b + c
    num_k = 4 * r * math.sin(a) / 2 * math.sin(c) / 2
    num_l = a * x + b / c * x + d
    num_n = 2 * math.sin(a) + b / 2 * math.cos(a) - b / 2
    num_m = math.abs(2 * math.sin(-3 * math.abs(x/2)))



def exercise1_18():
    k = int(input("Введіть k"))
    s = 5
    s = 57
    print(f"В номері а s={s}")
    s =6
    s = -5.2 * 6
    s =0
    print(f"В номері б s={s}")
    s = -7.5
    s = 2 * s
    print(f"В номері в s={s}")
    s = 45
    s = -25
    s = s + k
    print(f"В номері г s={s}")

def exercise1_19():
    k = int(input("Введіть k"))
    x = 10
    x = -10
    print(f"В номері а x={x}")
    x= 17.5
    x= -2 * x
    print(f"В номері б x={x}")
    x = 60
    x = x - 1
    x = 0
    print(f"В номері в x={x}")
    x = -50
    x = -25
    x = x + k
    print(f"В номері г x={x}")


def exercise1_20():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    a = 5.8
    b = -7.9
    b = a
    a = b
    print(f"В номері A a={a} b={b}")


def exercise1_21():
    a = 5.8
    b = -7.9
    c = a
    a = b
    b = c
    print(f'a={a}\n,b={b}')


def exercise1_22():
    x = int(input("Введіть x"))
    y = 7 * pow(x, 2) - 3 * x + 6
    print(y)

    a = int(input("Введіть a"))
    f = 12 * pow(a, 2) + 7 * a - 16
    print(f)


def exercise1_23():
    import math
    a = int(input())
    y = (pow(a, 2) + 10) / (math.sqrt(pow(a, 2) + 1))
    print(int(y))


def exercise1_24():
    a = input("Введіть a")
    x = math.sqrt((2 * a + math.sin(math.fabs(3 * a))) / 3.56)
    print(f'x={x}')

    x = input("Введіть x")
    y = math.sin((3.2 + math.sqrt(1 + x)) / math.fabs(5 * x))
    print(f'y={y}')


def exercise1_25():
    a = int(input())
    print(a * 4)


def exercise1_26():
    r = int(input())
    o = 2 * math.pi * r
    print(o)


def exercise1_28():
    len = random.randint(0, 10)
    vol = len ** 3
    sqr = len ** 2
    print(f"Ребро={len} об'єм={vol} площа={sqr}")


def exercise1_29():
    r = random.randint(0, 50)
    len = 2 * math.pi * r
    print(f'Radius={r} length={len}')


def exercise1_30a():
    x = int(input("Введіть x"))
    y = int(input("Введіть y"))
    z = pow(x, 3) - 2.5 * x * y + 1.78 * pow(x, 2) - 2.5 * y + 1
    print(z)


def exercise1_30b():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    x = 3.56 * a + pow(b, 3) - 5.8 * b ** 2 + 3.8 * a - 1.5
    print(x)


def exercise1_31():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    av_ar = (a + b) / 2
    av_geom = math.sqrt(a * b)
    print(f"Середнє арифметичне={av_ar} , а середнє геометричне={av_geom}")


def exercise1_32():
    vol = random.randint(0, 50)
    weigth = random.randint(0, 50)
    density = weigth / vol
    print(f'Об єм={vol} маса={weigth} щільність={density}')


def exercise1_33():
    count = random.randint(0, 1000)
    sqr = random.randint(0, 1000)
    density = count / sqr
    print(f'кількість населення{count} площа{sqr} щільність{density}ос/км квадраьний')


def exercise1_34():
    # ax+b=0
    a = float(input('Введіть a'))
    b = float(input('Введіть b'))
    x = -1 * b / a
    print(f'a={a} b={b} x={x}')


def exercise1_35():
    c1 = random.randint(0, 10)
    c2 = random.randint(0, 10)
    gipotenuza = math.sqrt(c1 ** 2 + c2 ** 2)
    print(f'Перший катет ={c1} другий катет={c2} гіпотенуза={gipotenuza}')


def exercise1_36():
    r1 = 5
    r2 = 7
    sqrt = math.pi * r2 ** 2 - math.pi * r1 ** 2
    print(f'Площа кільця={sqrt}')


def exercise1_37():
    c1 = random.randint(0, 10)
    c2 = random.randint(0, 10)
    gipotenuza = math.sqrt(c1 ** 2 + c2 ** 2)
    print(f'Перший катет ={c1} другий катет={c2} гіпотенуза={gipotenuza}')
    per = c1 + c2 + gipotenuza
    print(f'Периметр={per}')


def exercise1_39():
    x = int(input("Введіть x"))
    y = int(input("Введіть y"))
    z = (x + ((2 + y) / x ** 2)) / (y + (1 / (math.sqrt(x ** 2 + 10))))
    q = 2.8 * math.sin(x) + math.fabs(y)
    print(z)
    print(q)
    print(math.fabs(x))


def exercise1_40():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    x = ((2 / (a ** 2 + 25)) + b) / (math.sqrt(b) + ((a + b) / 2))
    y = (math.fabs(a) + 2 * math.sin(b)) / 5.5 * a
    print(x)
    print(y)


def exercise1_41():
    e = int(input("Введіть e"))
    f = int(input("Введіть f"))
    g = int(input("Введіть g"))
    h = int(input("Введіть h"))
    a = math.sqrt(math.fabs(e - (3 / f)) ** 3 + g)
    b = math.sin(e) + math.cosh(h) ** 2
    c = (33 * g) / (e * f - 3)
    print(a)
    print(b)
    print(c)


def exercise1_42():
    e = int(input("Введіть e"))
    f = int(input("Введіть f"))
    g = int(input("Введіть g"))
    h = int(input("Введіть h"))
    a = (e + (f / 2)) / 3
    b = math.fabs(h ** 2 - g)
    c = math.sqrt((g - h) ** 2 - 3 * math.sin(e))
    print(a)
    print(b)
    print(c)


def exercise1_43():
    e = int(input("Введіть e"))
    f = int(input("Введіть f"))
    average = (math.fabs(e) + math.fabs(f)) / 2
    geom_av = (math.sqrt(math.fabs(e) * math.fabs(f)))
    print(average)
    print(geom_av)


def exercise1_44():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    p = a * b
    diagonal = math.sqrt(a ** 2 + b ** 2)
    print(f"Периметр={p}")
    print(f"Діагональ={diagonal}")


def exercise1_45():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    addition = a + b
    substraction = a - b
    multiplication = a * b
    q = b % a
    print(addition)
    print(substraction)
    print(multiplication)
    print(q)


def exercise1_46(a, b, c):
    volume = a * b * c
    square = a * b
    print(volume)
    print(square)


def exercise1_47(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)


def exercise1_52():
    price_candy = 50
    price_cookie = 40
    price_apple = 20
    x = int(input("Скільки цукерок ви хочеш купити?"))
    y = int(input("Скільки печива ви хочете купити?"))
    z = int(input("Скільки яблук ти хочеш купити?"))
    cost = price_candy * x + price_cookie * y + price_apple * z
    print(cost)


def exercise1_53():
    price_monitor = 150
    price_block = 300
    price_keybord = 100
    price_mouse = 50
    total_price = price_mouse + price_monitor + price_block + price_keybord
    print(f'Комп коштує {total_price}')


def exercise1_54():
    tanyas_age = 15
    mitia_age = 20
    aver = (tanyas_age + mitis_age) / 2
    print(f'Тетьяна {tanyas_age - aver} Мітяй {mitia_age - aver}')


def exercise1_55():
    v1 = 60
    v2 = 70
    s = 500
    time = s / (v1 + v2)
    print(f'Автомобілі зустрінуться через {time} годин')


def exercise1_57():
    celsius = input("Введіть значення температури у цельсіях:")
    fahrenheit = int(celsius) * 1.8 + 32
    kelvin = int(celsius) + 273.15
    print(f"Цельсії{celsius} Фарангейт {fahrenheit} Кельвіни{kelvin}")


def exercise1_58():
    fahrenheit = 450
    celsiuis = (fahrenheit - 32) * 5 / 9
    print(f'Цельсії={celsiuis}')


def exercise1_59():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    c = a
    a = b
    b = c
    print(f"A={a},B={b}")


def exercise1_60():
    a = int(input("Введіть a"))
    b = int(input("Введіть b"))
    c = int(input("Введіть c"))
    b = a
    a = b
    c = a
    print(f"A={a},B={b},C={c}")
    b = a
    c = b
    a = c
    print(f"A={a},B={b},C={c}")


def exercise1_61():
    a = int(input("Впишіть a"))
    a2 = a * a
    a4 = a2 * a2
    print(f"a){a4}")
    a2 = a * a
    a6 = a2 * a2 * a2
    print(f"б){a6}")
    a3 = a * a * a
    a7 = a3 * a3 * a
    print(f"в){a7}")
    a2 = a * a
    a4 = a2 * a2
    a8 = a4 * a4
    print(f"г){a8}")
    a3 = a * a * a
    a9 = a3 * a3 * a3
    print(f"д){a9}")
    a2 = a * a
    a4 = a2 * a2
    a10 = a4 * a4 * a2
    print(f"е){a10}")
    a2 = a * a
    a4 = a2 * a2
    a13 = a4 * a4 * a4 * a
    print(f"ж){a13}")
    a2 = a * a
    a3 = a2 * a
    a6 = a3 * a3
    a15 = a6 * a6 * a3
    print(f"з){a15}")
    a2 = a * a
    a4 = a2 * a2
    a8 = a4 * a4
    a16 = a8 * a8
    a20 = a16 * a4
    a21 = a20 * a
    print(f"и){a21}")
    a2 = a * a
    a4 = a2 * a2
    a8 = a4 * a4
    a16 = a8 * a8
    a24 = a16 * a8
    a28 = a24 * a4
    print(f"к){a28}")
    a64 = a * a * a * a * a * a * a
    print(f"л){a64}")


def exercise2_1(cm):
    m = cm // 100;
    print(f"В {cm} сантиметрах = {m}повних метрів")


def exercise2_2(kg):
    c = kg // 100
    print(f"В {kg} kg = {c}повних центнерів")


def exercise2_3(kg):
    t = kg // 1000
    print(f"В {kg} kg = {t} повних кілограмів")


def exercise2_4(m):
    km = m // 1000
    print(f"В {m} m = {km}повних km")


def exercise2_5():
    weeks = 234 // 7
    print(f"Пройшло{weeks}тижнiв")


def exercise2_6():
    n = 1655
    print((n % 3600) // 60)
    print((n % 60) // 60)


def exercise2_7():
    length = 543
    print(length // 130)


def exercise2_10():
    n = 25
    print(n // 10)
    print(25 // 1)
    print(n // 10 + n % 10)
    print((n // 10) * (n % 10))

def exercise2_11():
    n = 25
    n2=str((n // 10))
    n1=str((n % 10))
    print(n1+n2)

def exercise2_12():
    n = 251
    print(n // 1)
    print(25 // 10)
    print(n // 10 +n//100+ n % 10)
    print((n//100)*(n // 10) * (n % 10))

def exercise2_13():
    n=str(251)
    print(n[2]+n[1]+n[0])

def exercise2_14():
    n = str(251)
    print(  n[1] + n[0]+n[2])

def exercise2_15():
    n = str(251)
    print( n[2]+n[1] + n[0] )

def exercise2_16():
    n = str(251)
    print(n[2] + n[1] + n[0])


