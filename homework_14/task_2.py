# 2)	Если в функцию передается кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нем. Число - количество нечетных цифр.
# Строка - количество букв.

def func1(x):
    if type(x) == tuple:
        return sum(len(i) for i in x if i.isalpha())
    if type(x) == list:
        return sum([len(str(i)) for i in x if str(i).isalpha() or str(i).isdigit()])
    if type(x) == int:
        return len([str(i) for i in str(x) if int(i) % 2 == 0])
    if type(x) == str:
        return len(x)
print(func1('abcde'))