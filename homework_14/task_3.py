# 3)	Функция для вывода таблицы умножения для указанного числа.

def tabl(x):
    n = 1
    while True:
        if n == 11:
            print('Таблица завершена')
            break
        print(x * n)
        n += 1
print(tabl(9))