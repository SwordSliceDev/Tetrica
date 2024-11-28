def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__
        print(args)
        print(annotations)
        if len(args) != len(annotations):
            raise TypeError(f'В {func.__name__} получено неверное кол-во аргументов: {len(args)}, ожидается: {len(annotations)}')

        for (param_name, param_type), arg_value in zip(annotations.items(), args):
            if not isinstance(arg_value, param_type):
                raise TypeError(f'Аргумент {param_name} должен иметь тип {param_type.__name__} вместо {type(arg_value).__name__}')
        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int):
    return a+b
