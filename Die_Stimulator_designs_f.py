from random import *
from function import*

a = "|"
d = "It's a"
p = {1: a, 2: (a * 2), 3: (a * 3), 4: (a * 4), 5: (a * 5), 6: (a * 6)}
f = {1: "i", 2: "ii", 3: "iii", 4: "iv", 5: "v", 6: "vi"}
e = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}
s = randint(1, 6)


def func_type_1():
    s = randint(1, 6)
    print("[--------]")
    print("[" + d.center(8) + "]")
    print("[" + p[s].center(8) + "]")
    print("[" + str(s).center(8) + "]")
    print("[--------]")


def func_type_2():
    s = randint(1, 6)
    print(" ________")
    print("[        ]")
    print("|" + d.center(8) + "|")
    print("|" + p[s].center(8) + "|")
    print("|" + str(s).center(8) + "|")
    print("[________]")


def func_type_3():
    s = randint(1, 6)
    print("/" * 10)
    print("\\" + d.center(8) + "\\")
    print("/" + p[s].center(8) + "/")
    print("\\" + str(s).center(8) + "\\")
    print("/" * 10)


def func_type_4():
    s = randint(1, 6)
    print("/" * 10)
    print("/" + d.center(8) + "/")
    print("/" + p[s].center(8) + "/")
    print("/" + str(s).center(8) + "/")
    print("/" * 10)


def func_type_5():
    s = randint(1, 6)
    print("||||||||||")
    print("|" + d.center(8) + "|")
    print("|" + p[s].center(8) + "|")
    print("|" + str(s).center(8) + "|")
    print("||||||||||")


def func_type_6():
    s = randint(1, 6)
    print("||||||||||")
    print("|" + d.center(8) + "|")
    print("|" + f[s].center(8) + "|")
    print("|" + str(s).center(8) + "|")
    print("||||||||||")


def func_type_7():
    s = randint(1, 6)
    print("||||||||||")
    print("|" + d.center(8) + "|")
    print("|" + e[s].center(8) + "|")
    print("|" + str(s).center(8) + "|")
    print("||||||||||")


def func_type_8():
    s = randint(1, 6)
    print("[--------]")
    print("[" + d.center(8) + "]")
    print("[" + e[s].center(8) + "]")
    print("[" + str(s).center(8) + "]")
    print("[--------]")


def func_type_9():
    s = randint(1, 6)
    print("/" * 10)
    print("/" + d.center(8) + "/")
    print("/" + f[s].center(8) + "/")
    print("/" + str(s).center(8) + "/")
    print("/" * 10)


def func_type_10():
    s = randint(1, 6)
    print("/" * 10)
    print("\\" + d.center(8) + "\\")
    print("/" + f[s].center(8) + "/")
    print("\\" + str(s).center(8) + "\\")
    print("/" * 10)


def func_type_11():
    s = randint(1, 6)
    print("/" * 10)
    print("\\" + d.center(8) + "\\")
    print("/" + e[s].center(8) + "/")
    print("\\" + str(s).center(8) + "\\")
    print("/" * 10)


