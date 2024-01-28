import random
# print("Крутые фишечки")
# print("Двоичная система исчисления: ")
# a = int(input("Введите число: "))
# b = []
# while a != 0:
#     if a%2 == 1:
#         b += "1"
#         a = a//2
#     else:
#         b += "0"
#         a = a/2
# b = list(reversed(b))
# for i in b:
#     print(i, end="")
# a = input("\nХочеш перевести наоборот? ")
# while a == "да":
#     x = int(input("Введи ка числецо: "),2)
#     print(x)
#     a = input("Хочеш перевести наоборот ещё? ")
# print("\nКалькулятор-чан")
# s = 0
# w = 0
# all = 0
# dfg = "да"
# while dfg == "да":
#     for i in range(0,100):
#         all += 1
#         a = random.randint(1, 10)
#         j = random.randint(1, 10)
#         p = int(input(f"{a} * {j} = "))
#         if p == (a*j):
#             print(f"Да! {a} * {j} = {p}")
#             w += 1
#             print('Твой счет: ',w)
#         else:
#             print(f"Не! {a} * {j} = {a*j}, а не {p}")
#             print('Твой счет: ',w)
#     print(f"Ты знаешь {(w/10)*100}% таблице умножения!")
#     if w > 99:
#         print("Ухты! Ничего себе, но не стоит останавливаться.\nТы заработал {w} c {all}")
#     else:
#         print(f"Ты хоть старался? \nТы заработал {w} c {all}")
#     dfg = input("Хочешь повторить? ")
# a=0 
# for i in range (1,5): 
#     a=a+10 
# print(a)


# import tkinter as tk
# import random

# def check_answer():
#     global w, all
#     user_answer = answer_entry.get()
#     if user_answer.isdigit():
#         user_answer = int(user_answer)
#         if user_answer == (a * j):
#             result_label.config(text=f"Да! {a} * {j} = {user_answer}")
#             w += 1
#             score_label.config(text=f'Твой счет: {w}')
#         else:
#             result_label.config(text=f"Не! {a} * {j} = {a*j}, а не {user_answer}")
#     else:
#         result_label.config(text="Пожалуйста, введите число.")

#     all += 1
#     next_question()

# def next_question():
#     global a, j
#     a = random.randint(1, 10)
#     j = random.randint(1, 10)
#     question_label.config(text=f"{a} * {j} = ")
#     answer_entry.delete(0, tk.END)

# def repeat():
#     global w, all
#     w = 0
#     all = 0
#     score_label.config(text='Твой счет: 0')
#     next_question()
#     repeat_button.config(state=tk.DISABLED)

# w = 0
# all = 0

# root = tk.Tk()
# root.title("Калькулятор-чан")

# question_label = tk.Label(root, text="", font=("Arial", 24))
# question_label.pack()

# answer_entry = tk.Entry(root, font=("Arial", 24))
# answer_entry.pack()

# check_button = tk.Button(root, text="Проверить", command=check_answer, font=("Arial", 18))
# check_button.pack()

# result_label = tk.Label(root, text="", font=("Arial", 18))
# result_label.pack()

# score_label = tk.Label(root, text="Твой счет: 0", font=("Arial", 18))
# score_label.pack()

# repeat_button = tk.Button(root, text="Повторить", command=repeat, font=("Arial", 18))
# repeat_button.pack()
# repeat_button.config(state=tk.DISABLED)

# next_question()

# root.mainloop()


import tkinter as tk
import random
import time

def check_answer():
    global w, all, start_time
    user_answer = answer_entry.get()
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if user_answer == (a * j):
            result_label.config(text=f"Да! {a} * {j} = {user_answer}")
            w += 1
            score_label.config(text=f'Твой счет: {w}')
        else:
            result_label.config(text=f"Не! {a} * {j} = {a*j}, а не {user_answer}")
    else:
        result_label.config(text="Пожалуйста, введите число.")

    all += 1
    next_question()

def next_question():
    global a, j, start_time
    a = random.randint(1, 10)
    j = random.randint(1, 10)
    question_label.config(text=f"{a} * {j} = ")
    answer_entry.delete(0, tk.END)
    start_time = time.time()  # Запуск таймера

def repeat():
    global w, all, start_time
    w = 0
    all = 0
    score_label.config(text='Твой счет: 0')
    next_question()
    repeat_button.config(state=tk.DISABLED)

w = 0
all = 0

root = tk.Tk()
root.title("Калькулятор-чан")

question_label = tk.Label(root, text="", font=("Arial", 24))
question_label.pack()

answer_entry = tk.Entry(root, font=("Arial", 24))
answer_entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_answer, font=("Arial", 18))
check_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack()

score_label = tk.Label(root, text="Твой счет: 0", font=("Arial", 18))
score_label.pack()

repeat_button = tk.Button(root, text="Повторить", command=repeat, font=("Arial", 18))
repeat_button.pack()
repeat_button.config(state=tk.DISABLED)

start_time = time.time()  # Инициализация таймера

next_question()

root.mainloop()