# Задание № Алгоритм
# 1. Даны два значения ( numbers , desired_sum )
# 2. Первая это список из чисел
# 3. Вторая это число которое должно получиться из двух чисел
# Смысл :
# Нужно сделать так чтобы возвращался индекс двух чисел которые в сумме возвращают желаемую сумму
# Например есть список из таких чисел [2, 7, 11, 15] желаемая сумма является число 9 , значит должен
# возвращаться индекс [0, 1] потому что только сумма этих двух чисел является желаемой
# Подсказка : Нужно использовать циклы for

 # def ara(disired_sum):
desired_sum = 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

c = 0
for i in numbers:
    if i + numbers[c] == desired_sum:
        print(i), print(numbers[c])
    else:
        continue
c = c + 1
print(c)
