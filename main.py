import random  #импортируем модуль random

spisok=[random.randint(-10, 10) for _ in range(20)] #генерируем список случайных чисел в диапозоне от -10 до 10
print("список значений: ", spisok) #вывод списка

pairs=[] # инициализация переменной 
for i in range(len(spisok)): # цикл for для создание уникальных пар в spisok
    for j in range(i+1, len(spisok)):
        pairs.append((spisok[i], spisok[j])) # добавляем пару [i] [j] в pairs

print("\nвсе уникальные пары: ", pairs) #вывод

num=int(input("введите целое число: ")) #запрос у пользователя 

count=0 #инициализация для подсчета
for pair in pairs: #цикл for 
    if sum(pair)<num: #проверка на то у кого меньше
        count+=1 #увелечение счетчика

print(f"\nкол-во пар, чья сумма меньше {num}: {count}") #вывод