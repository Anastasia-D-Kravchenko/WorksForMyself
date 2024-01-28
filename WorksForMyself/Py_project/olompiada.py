# #/////////////////////////////////Квадрат суми//////////////////////////////////////////
# n = input().strip()
# a = 0
# for i in n:
#     a += int(i)
# a = a ** 2
# print(a)
# #/////////////////////////////////Сума парних цифр//////////////////////////////////////////
# n = input().strip()
# a = 0
# for i in n:
#     if int(i) % 2 == 0:
#         a += int(i)
# print(a)
# #/////////////////////////////////Зайва цифра//////////////////////////////////////////
# n = input().strip()
# a = []
# for i in n:
#     a.append(int(i))
# c = 0
# d = []
# for i in range(len(a)):
#     b = a.copy()
#     b.pop(i)
#     d.append(int("".join(map(str, b))))
# print(max(d))
# #/////////////////////////////////Обміняти max і min//////////////////////////////////////////
# a = int(input().strip())
# b = input().strip().split()
# max = max(map(int, b))
# min = min(map(int, b))
# for i in range(a):
#     if int(b[i]) == int(max):
#         b[i] = min
#     elif int(b[i]) == int(min):
#         b[i] = max
# print(" ".join(map(str, b)))
# #/////////////////////////////////Сир для Анфіси - 2//////////////////////////////////////////
# a, b, c = map(int, input().split())
# z = a*b*c-1
# print(z)
# def fun1(*x):
#     print(x)
# fun1(5,6,7)
a = float(input("Введіть довжину відрізка a: "))
b = float(input("Введіть довжину відрізка b: "))
c = float(input("Введіть довжину відрізка c: "))
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Можна побудувати прямокутний трикутник.")
else:
    print("Не можна побудувати прямокутний трикутник.")