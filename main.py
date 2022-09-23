import itertools
import math


def prime(num):
    count = 0
    for i in itertools.count(2):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            count += 1
        if count == num:
            return i


while True:
    try:
        number = int(input("Введите номер простого числа "))
        print(prime(number))
        break
    except ValueError:
        print("Hекорректный ввод")
