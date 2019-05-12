def decor_fn(func):
    def other_fn(*args,**kwargs):
        result=func(*args,**kwargs)
        print("Работает декоратор. Оригинальная функция вернула: ",result)
        return result+" + decor"
    return other_fn

@decor_fn
def simple_fn(a):
    print("Вызов оригинальной функции") # указывает на вызов оригинальной функции
    return a

print(simple_fn("TEST"))
