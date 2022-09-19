def options(arg):
    if isinstance(arg, list):
        count = 0
        for i in arg:
            if i % 2 == 0:
                count += 1
            if i < 0:
                arg.remove(i)
        return max(arg), count, arg
    elif isinstance(arg, dict):
        sort_dict = dict(sorted(arg.items(), key=lambda item: item[1], reverse=True))
        return sort_dict
    elif isinstance(arg, int):
        new_number = ''
        if arg < 0:
            new_number += '-'
        new_number += str(abs(arg))[::-1]
        return new_number
    else:
        count_dict = {}
        for i in arg:
            temp = {i: arg.count(i)}
            count_dict.update(temp)
        return count_dict


while True:
    choice = 0
    print('''Выберите структуру данных для работы:
    1. Список
    2. Словарь
    3. Целочисленное число
    4. Строка
    ''')
    try:
        choice = int(input(">>"))
        break
    except:
        print("Некорректный ввод")

value = 0
if choice == 1:
    value = list(map(int, input("Введите список ").split()))
elif choice == 2:
    value = {}
    size = int(input("Введите длинну словаря"))
    for number in range(size):
        key_val = input("Введите ключ ")
        val = input("Введите значение ")
        temp = {key_val: val}
        value.update(temp)
elif choice == 3:
    while True:
        try:
            value = int(input("Введите целое число "))
            break
        except:
            print("Некорректный ввод целочисленного числа")
elif choice == 4:
    value = input("Введите строку ")
else:
    print("Некорректный пункт меню")

res = options(value)

if choice == 1:
    print('Максимальный элемент', res[0])
    print('Количество четных', res[1])
    print('Список без отрицательных', *res[2])
elif choice == 2:
    print('Отсортированный словарь', res)
elif choice == 3:
    print('Перевернутое число', res)
elif choice == 4:
    print('Количество вхождений каждого символа', res)

# value = int(input())
# value = list(map(int, input().split()))
# value = input()
# value = {'q': 2, 'e': 1}
# print(options(value))
