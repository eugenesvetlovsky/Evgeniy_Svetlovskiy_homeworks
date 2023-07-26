# 4)	Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(),
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные: название анализируемой функции,
# наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.)
# . Попробуйте повторить результат девушки.

import inspect

def inspect_function(func):
    func_name = func.__name__
    print(f'Функция: {func_name}')
    func_params = inspect.signature(func).parameters
    for param_name, param in func_params.items():
        param_type = param.annotation
    print(f'Параметр: {param_name}')
    print(f'Тип: {param_type}')

def func1(par1:int, par2:str, par3:float):
    pass

inspect_function(func1)

# Не понял почему выводится только последняя пара par3 class float