# 1)	Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.
# Операции являются функциями.Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

num1 = float(input('Введите первое число '))
znak = input('Введите знак ')
num2 = float(input('Введите второе число '))

def sum(num1, num2):
    return num1 + num2
def razn(num1, num2):
    return num1 - num2
def proizv(num1, num2):     # произведение
    return num1 * num2
def chastn(num1, num2):     # частное
    return num1 / num2
def error(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    finally:
        print('Программа завершена.')

if znak == '/' and num2 == 0:
    print(error(num1, num2))
elif znak == '+':
    print(sum(num1, znak, num2))
elif znak == '-':
    print(razn(num1, znak, num2))
elif znak == '*':
    print(proizv(num1, znak, num2))
else:
    print(chastn(num1, znak, num2))
