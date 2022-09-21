try:
    a = int(input("Делимое "))
    b = int(input("Делитель "))
    print('Частное ', a/b)
except ValueError:
    print("Введите целочисленное значение")
except ZeroDivisionError:
    print("Деление на ноль запрещено")
else:
    print("Деление прошло успешно")
finally:
    print("Программа завершена")
