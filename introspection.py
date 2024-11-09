import inspect
def introspection_info(obj):
    type_obj = type(obj).__name__ #Тип объекта
    attr_obj = dir(obj) #Атрибуты объекта
    meth_obj = [method for method in attr_obj if callable(getattr(obj, method))] #Методы объекта
    module_obj = obj.__class__.__module__ #Модуль объекта
    if inspect.isclass(obj) == False: #Пример мриминения модуля inspect. Самоанализ объекта на класс
        print(f'{obj} - это не класс')
        if isinstance(obj, int): #Проверка объекта на его принадлежность к int
            print(f'{obj} - это число')
        else:
            print(f'{obj} - это что то другое')

    data_dict = {'Тип': type_obj, 'Атрибуты': attr_obj, 'Методы': meth_obj, 'Модуль': module_obj} #словарь с данными об объекте
    return data_dict #Возврат словаря с данными об объекте


number_info = introspection_info(42)
print(number_info)
print()
number_info = introspection_info('Персональный компьютер')
print(number_info)
print()
number_info = introspection_info([42, 38, 'кровать'])
print(number_info)